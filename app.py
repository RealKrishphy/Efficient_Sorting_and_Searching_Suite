from flask import Flask, request, jsonify
from flask_cors import CORS
import random, time

app = Flask(__name__)
CORS(app)

def bubble_sort(arr):
    n = len(arr)
    comps = swaps = 0
    start = time.time()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comps += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return arr, comps, swaps, round(time.time() - start, 5)

def merge_sort(arr):
    comps = swaps = 0
    start = time.time()

    def merge(left, right):
        nonlocal comps, swaps
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comps += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                swaps += 1
        result += left[i:]
        result += right[j:]
        return result

    def divide(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        left = divide(lst[:mid])
        right = divide(lst[mid:])
        return merge(left, right)

    sorted_arr = divide(arr)
    return sorted_arr, comps, swaps, round(time.time() - start, 5)

def quick_sort(arr):
    comps = swaps = 0
    start = time.time()

    def _quick(lst):
        nonlocal comps, swaps
        if len(lst) <= 1:
            return lst
        pivot = random.choice(lst)
        left, middle, right = [], [], []
        for x in lst:
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)
        comps += len(lst) - 1
        swaps += len(left) + len(right)
        return _quick(left) + middle + _quick(right)

    sorted_arr = _quick(arr)
    return sorted_arr, comps, swaps, round(time.time() - start, 5)


def generate_dataset(size):
    random.seed(42)
    if size <= 50:
        return [random.randint(1, 500) for _ in range(size)]
    elif size <= 200:
        return [random.randint(1, 2000) for _ in range(size)]
    else:
        return [random.randint(1, 5000) for _ in range(size)]


@app.route('/sort', methods=['GET'])
def sort_data():
    algo = request.args.get('algo', 'bubble')
    size = int(request.args.get('size', 50))
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
    app.run(host='0.0.0.0', port=8080, debug=True)
