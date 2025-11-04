from flask import Flask, request, jsonify
from flask_cors import CORS
import algorithms as algorithm
import utils

app = Flask(__name__)
CORS(app)

@app.route('/compare', methods=['POST'])
def compare_all():
    data = request.get_json() or {}
    arr = data.get('array', [])
    if not arr:
        size = int(data.get('size', 50))
        arr = utils.generate_dataset(size)
    if not isinstance(arr, list) or not all(isinstance(x, int) for x in arr):
        return jsonify({"error": "array must be a list of integers"}), 400

    b_sorted, b_comps, b_swaps, b_time = algorithm.bubble_sort(arr.copy())
    q_sorted, q_comps, q_swaps, q_time = algorithm.quick_sort(arr.copy())
    m_sorted, m_comps, m_swaps, m_time = algorithm.merge_sort(arr.copy())

    return jsonify({
        "original": arr,
        "bubble": {
            "name": "Bubble Sort",
            "sorted": b_sorted,
            "comparisons": b_comps,
            "swaps": b_swaps,
            "time": b_time,
            "time_complexity": "O(n²)",
            "space_complexity": "O(1)"
        },
        "quick": {
            "name": "Quick Sort",
            "sorted": q_sorted,
            "comparisons": q_comps,
            "swaps": q_swaps,
            "time": q_time,
            "time_complexity": "O(n log n)",
            "space_complexity": "O(log n)"
        },
        "merge": {
            "name": "Merge Sort",
            "sorted": m_sorted,
            "comparisons": m_comps,
            "swaps": m_swaps,
            "time": m_time,
            "time_complexity": "O(n log n)",
            "space_complexity": "O(n)"
        }
    })

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
