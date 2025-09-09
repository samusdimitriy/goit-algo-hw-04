import timeit
import random

def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def timsort_simulation(arr):
    return insertion_sort(arr) if len(arr) <= 32 else merge_sort(arr)

algorithms = {
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "Timsort": timsort_simulation,
    "Python": lambda arr: sorted(arr)
}

sizes = [100, 10000]
data_types = {
    "random": lambda n: [random.randint(1, n) for _ in range(n)],
    "sorted": lambda n: list(range(n)),
    "reversed": lambda n: list(range(n, 0, -1))
}

for data_name, data_func in data_types.items():
    print(f"{data_name}:")
    for size in sizes:
        data = data_func(size)
        for name, func in algorithms.items():
            time_taken = timeit.timeit(lambda: func(data), number=1)
            print(f"  {name} n={size}: {time_taken:.4f}s")
    print()
