from flask import Flask, request, jsonify
from flask_cors import CORS
from algorithms import bubble_sort, merge_sort, quick_sort
from utils import generate_dataset, get_hardcoded_dataset

app = Flask(__name__)
CORS(app)

@app.route('/sort', methods=['GET'])
def sort_data():
    algo = request.args.get('algo', 'bubble')
    size = int(request.args.get('size', 50))
    mode = request.args.get('mode', 'random')

    if mode == 'hardcoded':
        data = get_hardcoded_dataset()
    else:
        data = generate_dataset(size)

    if algo == 'bubble':
        sorted_arr, comps, swaps, duration = bubble_sort(data.copy())
    elif algo == 'merge':
        sorted_arr, comps, swaps, duration = merge_sort(data.copy())
    else:
        sorted_arr, comps, swaps, duration = quick_sort(data.copy())

    return jsonify({
        "algorithm": algo.title() + " Sort",
        "comparisons": comps,
        "swaps": swaps,
        "time": duration,
        "sorted_data": sorted_arr
    })

if __name__ == '__main__':
    app.run(debug=True)
