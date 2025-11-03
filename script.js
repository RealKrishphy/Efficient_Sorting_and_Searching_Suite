const API_BASE = "http://127.0.0.1:8080";

function visualizeArray(arr, animate = true) {
  const bars = document.getElementById("bars");
  bars.innerHTML = "";
  if (!arr || arr.length === 0) return;

  const max = Math.max(...arr);
  const n = arr.length;
  const displayLimit = n > 300 ? 5 : 1;
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

  arr.forEach((v, i) => {
    if (i % displayLimit !== 0) return;
    const b = document.createElement("div");
    b.className = "bar";
    const h = (v / max) * 100;

    const cIndex = Math.floor((v / max) * (plasma.length - 1));
    b.style.background = plasma[cIndex];

    if (animate && n <= 300) {
      b.style.height = "0%";
      setTimeout(() => (b.style.height = `${h}%`), i * 1);
    } else {
      b.style.height = `${h}%`;
    }
    bars.appendChild(b);
  });
}

async function fetchSorted(algo, size) {
  const res = await fetch(`${API_BASE}/sort?algo=${algo}&size=${size}`);
  return res.ok ? res.json() : null;
}

function shuffleArray(n) {
  return Array.from({ length: n }, () => Math.floor(Math.random() * 5000));
}

document.getElementById("sortBtn").addEventListener("click", async () => {
  const algo = document.getElementById("algo").value;
  const size = parseInt(document.getElementById("size").value, 10);
  const data = await fetchSorted(algo, size);

  if (!data) {
    alert("Backend not available. Start Flask app.");
    return;
  }

  document.getElementById("algoName").textContent = data.algorithm;
  document.getElementById("comparisons").textContent = data.comparisons;
  document.getElementById("swaps").textContent = data.swaps;
  document.getElementById("time").textContent = data.time + "s";

  visualizeArray(data.sorted_data, true);
});

document.getElementById("shuffleBtn").addEventListener("click", () => {
  const size = parseInt(document.getElementById("size").value, 10);
  visualizeArray(shuffleArray(size), true);
});

document.getElementById("autoBtn").addEventListener("click", async () => {
  const size = parseInt(document.getElementById("size").value, 10);
  let chosen = "quick";
  if (size <= 50) chosen = "bubble";
  else if (size <= 200) chosen = "merge";

  const data = await fetchSorted(chosen, size);
  if (!data) {
    alert("Backend not available. Start Flask app.");
    return;
  }

  document.getElementById("algoName").textContent = data.algorithm;
  document.getElementById("comparisons").textContent = data.comparisons;
  document.getElementById("swaps").textContent = data.swaps;
  document.getElementById("time").textContent = data.time + "s";

  visualizeArray(data.sorted_data, true);
});
