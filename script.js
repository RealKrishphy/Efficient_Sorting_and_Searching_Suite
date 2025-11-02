const API_BASE = 'http://127.0.0.1:5000';
async function fetchSorted(algo, size) {
try {
const res = await fetch(`${API_BASE}/sort?algo=${algo}&size=${size}`);
return await res.json();
} catch (err) {
alert('Backend not running. Start Flask app first.');
return null;
}
}
function visualizeArray(arr) {
const bars = document.getElementById('bars');
bars.innerHTML = '';
const max = Math.max(...arr);
arr.forEach(value => {
const bar = document.createElement('div');
bar.className = 'bar';
bar.style.height = `${(value / max) * 100}%`;
bars.appendChild(bar);
});
}
function shuffleArray(n) {
return Array.from({length: n}, () => Math.floor(Math.random() * 1000));
}
document.getElementById('sortBtn').addEventListener('click', async () => {
const algo = document.getElementById('algo').value;
const size = document.getElementById('size').value;
const data = await fetchSorted(algo, size);
if (data) {
document.getElementById('algoName').textContent = data.algorithm;
document.getElementById('comparisons').textContent = data.comparisons;
document.getElementById('swaps').textContent = data.swaps;
document.getElementById('time').textContent = data.time + 's';
visualizeArray(data.sorted_data);
}
});
document.getElementById('shuffleBtn').addEventListener('click', () => {
const size = parseInt(document.getElementById('size').value, 10);
visualizeArray(shuffleArray(size));
});
document.getElementById('autoBtn').addEventListener('click', async () => {
const size = parseInt(document.getElementById('size').value, 10);
let chosen = 'quick';
if (size <= 50) chosen = 'bubble';
else if (size > 500) chosen = 'merge';
document.getElementById('algo').value = chosen;
const data = await fetchSorted(chosen, size);
if (data) {
document.getElementById('algoName').textContent = data.algorithm;
document.getElementById('comparisons').textContent = data.comparisons;
document.getElementById('swaps').textContent = data.swaps;
document.getElementById('time').textContent = data.time + 's';
visualizeArray(data.sorted_data);
}
});
