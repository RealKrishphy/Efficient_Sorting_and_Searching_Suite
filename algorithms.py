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
    end = time.time()
    return sorted_arr, comps, swaps, round(end - start, 5)

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
