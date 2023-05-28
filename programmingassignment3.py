#Part1
def quicksort(arr, start, end):
    if start < end:
        pivot = arr[start]

        i = start + 1
        for j in range(start + 1, end + 1):
            if arr[j] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1

        arr[start], arr[i - 1] = arr[i - 1], arr[start]

        comparisons = end - start
        comparisons += quicksort(arr, start, i - 2)
        comparisons += quicksort(arr, i, end)

        return comparisons
    else:
        return 0


with open("QuickSort.txt") as file:
    integers = [int(line.strip()) for line in file]

comparisons = quicksort(integers, 0, len(integers) - 1)

print("Total number of comparisons:", comparisons)

#Part2
def quicksort(arr, start, end):
    if start < end:
        arr[start], arr[end] = arr[end], arr[start]
        pivot = arr[start]

        i = start + 1
        for j in range(start + 1, end + 1):
            if arr[j] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1

        arr[start], arr[i - 1] = arr[i - 1], arr[start]

        comparisons = end - start
        comparisons += quicksort(arr, start, i - 2)
        comparisons += quicksort(arr, i, end)

        return comparisons
    else:
        return 0


with open("QuickSort.txt") as file:
    integers = [int(line.strip()) for line in file]

comparisons = quicksort(integers, 0, len(integers) - 1)

print("Total number of comparisons:", comparisons)

#Part3
def get_median_index(arr, start, mid, end):
    if arr[start] < arr[mid]:
        if arr[mid] < arr[end]:
            return mid
        elif arr[start] < arr[end]:
            return end
        else:
            return start
    else:
        if arr[start] < arr[end]:
            return start
        elif arr[mid] < arr[end]:
            return end
        else:
            return mid


def quicksort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        median_index = get_median_index(arr, start, mid, end)
        arr[start], arr[median_index] = arr[median_index], arr[start]
        pivot = arr[start]

        # Partition the array
        i = start + 1
        for j in range(start + 1, end + 1):
            if arr[j] < pivot:
                arr[j], arr[i] = arr[i], arr[j]
                i += 1

        # Place the pivot in the correct position
        arr[start], arr[i - 1] = arr[i - 1], arr[start]

        # Recursively sort the left and right subarrays
        comparisons = end - start
        comparisons += quicksort(arr, start, i - 2)
        comparisons += quicksort(arr, i, end)

        return comparisons
    else:
        return 0



with open("QuickSort.txt") as file:
    integers = [int(line.strip()) for line in file]


comparisons = quicksort(integers, 0, len(integers) - 1)

print("Total number of comparisons:", comparisons)

