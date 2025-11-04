const API_BASE = "http://127.0.0.1:5050";
const route = "/compare";

// 🔹 Color palette
const plasma = [
  "#0d0887",
  "#41049d",
  "#6a00a8",
  "#8f0da4",
  "#b12a90",
  "#cc4778",
  "#e16462",
  "#f2844b",
  "#fca636",
  "#fcce25",
];
const barColor = (v, max) =>
  plasma[Math.floor((v / max) * (plasma.length - 1))];

// 🔹 DOM elements
const bars = {
  bubble: document.getElementById("bars-bubble"),
  quick: document.getElementById("bars-quick"),
  merge: document.getElementById("bars-merge"),
};
const stats = {
  bubble: document.getElementById("stats-bubble"),
  quick: document.getElementById("stats-quick"),
  merge: document.getElementById("stats-merge"),
};
const summary = document.getElementById("compare-summary");
const table = document.getElementById("comparison-table");
const sizeSelector = document.getElementById("size");

// 🎨 Smoothly render optimized bar graph
function renderBars(container, arr) {
  container.innerHTML = "";
  const n = arr.length;
  const maxBars = n > 120 ? 120 : n; // only 120 visible bars max
  const step = Math.floor(n / maxBars);
  const sampled = arr.filter((_, i) => i % step === 0).slice(0, 120);

  const max = Math.max(...sampled);
  sampled.forEach((v, i) => {
    const bar = document.createElement("div");
    bar.className = "bar";
    bar.style.background = barColor(v, max);
    bar.style.height = "0%"; // start from 0 height
    container.appendChild(bar);

    // smooth delayed animation
    setTimeout(() => {
      bar.style.height = (v / max) * 100 + "%";
    }, i * (1000 / sampled.length)); // evenly timed across bars
  });
}

// 🧮 Show stats below each chart
function showStats(id, data) {
  stats[id].innerHTML = `
    <div class="stat-item">Time: <strong>${data.time}s</strong></div>
    <div class="stat-item">Comparisons: <strong>${data.comparisons}</strong></div>
    <div class="stat-item">Swaps: <strong>${data.swaps}</strong></div>
    <div class="stat-item">Time Complexity: <strong>${data.time_complexity}</strong></div>
    <div class="stat-item">Space Complexity: <strong>${data.space_complexity}</strong></div>
  `;
}

// ✨ Highlight winner with smooth blue glow
function highlightBest(best) {
  ["bubble", "quick", "merge"].forEach((id) => {
    const card = document.getElementById("card-" + id);
    if (id === best) {
      card.classList.add("highlight");
    } else {
      card.classList.add("blurred");
    }
  });

  // remove highlight after a few seconds (optional)
  setTimeout(() => resetHighlight(), 3000);
}

// ♻️ Reset highlight and blur
function resetHighlight() {
  ["bubble", "quick", "merge"].forEach((id) => {
    const card = document.getElementById("card-" + id);
    card.classList.remove("highlight");
    card.classList.remove("blurred");
  });
}

// 🚀 Compare all algorithms
async function compareAll(size, highlight = false) {
  summary.textContent = "Analyzing algorithms...";
  resetHighlight();
  const res = await fetch(API_BASE + route, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ size }),
  });
  const data = await res.json();
  if (data.error) return alert(data.error);

  const algos = ["bubble", "quick", "merge"];
  algos.forEach((id) => {
    renderBars(bars[id], data[id].sorted);
    showStats(id, data[id]);
  });

  const best = algos.reduce((a, b) => (data[a].time < data[b].time ? a : b));
  summary.textContent = `🏆 Fastest: ${data[best].name} (${data[best].time}s)`;

  if (highlight) highlightBest(best);
  makeComparisonTable(data);
}

// 🧾 Comparison table generator
function makeComparisonTable(data) {
  table.innerHTML = `
  <h3>Algorithm Comparison Summary</h3>
  <table>
    <tr>
      <th>Algorithm</th><th>Time Complexity</th><th>Space Complexity</th>
      <th>Time (s)</th><th>Comparisons</th><th>Swaps</th>
    </tr>
    ${["bubble", "quick", "merge"]
      .map(
        (k) => `
      <tr>
        <td>${data[k].name}</td>
        <td>${data[k].time_complexity}</td>
        <td>${data[k].space_complexity}</td>
        <td>${data[k].time}</td>
        <td>${data[k].comparisons}</td>
        <td>${data[k].swaps}</td>
      </tr>
    `
      )
      .join("")}
  </table>`;
}

// 🎲 Shuffle dataset with animation
document.getElementById("shuffleBtn").onclick = () => {
  resetHighlight();
  const arr = Array.from(
    { length: parseInt(sizeSelector.value) },
    () => Math.floor(Math.random() * 500) + 1
  );
  Object.values(bars).forEach((b) => renderBars(b, arr));
  summary.textContent = "Dataset reshuffled — ready to compare!";
  table.innerHTML = "";
};

// 🧠 Compare All (no highlight)
document.getElementById("compareBtn").onclick = () =>
  compareAll(parseInt(sizeSelector.value), false);

// ⚡ Auto Select (highlight best)
document.getElementById("autoBtn").onclick = () =>
  compareAll(parseInt(sizeSelector.value), true);
