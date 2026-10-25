import random
import timeit

def insertion_sort(arr):
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
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

if __name__ == '__main__':
    data_small = [random.randint(0, 1_000) for _ in range(1_000)]
    data_medium = [random.randint(0, 10_000) for _ in range(10_000)]

    time_small_intertion = timeit.timeit(lambda: insertion_sort(data_small.copy()), number=5)
    time_small_merge = timeit.timeit(lambda: merge_sort(data_small.copy()), number=5)
    time_small_timsort = timeit.timeit(lambda: sorted(data_small.copy()), number=5)

    time_medium_intertion = timeit.timeit(lambda: insertion_sort(data_medium.copy()), number=5)
    time_medium_merge = timeit.timeit(lambda: merge_sort(data_medium.copy()), number=5)
    time_medium_timsort = timeit.timeit(lambda: sorted(data_medium.copy()), number=5)

    print(f"{'Algorithm': <20} | {'Time small data': <20} | {'Medium data (10k)':<18}")
    print(f":{'-'*19} | :{'-'*19}")
    print(f"{'Insertion sort': <20} | {time_small_intertion:<20.5f} | {time_medium_intertion:<20.5f}")
    print(f"{'Merge sort': <20} | {time_small_merge:<20.5f} | {time_medium_merge:<20.5f}")
    print(f"{'Time sort': <20} | {time_small_timsort:<20.5f} | {time_medium_timsort:<20.5f}")