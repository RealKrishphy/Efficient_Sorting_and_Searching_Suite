import time
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
    end = time.time()
    return arr, comps, swaps, round(end - start, 5)

def merge_sort(array):
    comparisons = exchanges = 0
    start_time = time.time()

    def merge(left_part, right_part):
        nonlocal comparisons, exchanges
        merged = []
        l_idx = r_idx = 0

        while l_idx < len(left_part) and r_idx < len(right_part):
            comparisons += 1
            if left_part[l_idx] <= right_part[r_idx]:
                merged.append(left_part[l_idx])
                l_idx += 1
            else:
                merged.append(right_part[r_idx])
                r_idx += 1
                exchanges += 1

        merged += left_part[l_idx:]
        merged += right_part[r_idx:]
        return merged

    def divide(sub_array):
        if len(sub_array) <= 1:
            return sub_array
        midpoint = len(sub_array) // 2
        left_half = divide(sub_array[:midpoint])
        right_half = divide(sub_array[midpoint:])
        return merge(left_half, right_half)

    sorted_array = divide(array)
    end_time = time.time()
    return sorted_array, comparisons, exchanges, round(end_time - start_time, 5)


def quick_sort(arr):
    import random
    comps = swaps = 0
    start = time.time()
    def _quick(lst):
        nonlocal comps, swaps
        if len(lst) <= 1:
            return lst
        pivot = random.choice(lst)
        left = [x for x in lst if x < pivot]
        middle = [x for x in lst if x == pivot]
        right = [x for x in lst if x > pivot]
        comps += len(lst) - 1
        swaps += len(left) + len(right)
        return _quick(left) + middle + _quick(right)
    sorted_arr = _quick(arr)
    end = time.time()
    return sorted_arr, comps, swaps, round(end - start, 5)
