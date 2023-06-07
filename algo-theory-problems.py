#Divide-and-conquer theoretical probelms
#Q: You are given as input an unsorted array of n distinct numbers, where n is a power of 2. 
#   Give an algorithm that identifies the second-largest number in the array, and that uses at most n + log2 n−2 comparisons.

import math

def find_second_largest(arr):
    n = len(arr)
    tournament_array = arr[:]
    challenger_array = []

    while len(tournament_array) > 1:
        next_round = []
        for i in range(0, len(tournament_array), 2):
            if tournament_array[i] > tournament_array[i + 1]:
                next_round.append(tournament_array[i])
                challenger_array.append(tournament_array[i + 1])
            else:
                next_round.append(tournament_array[i + 1])
                challenger_array.append(tournament_array[i])
        tournament_array = next_round

    largest = tournament_array[0]

    while len(challenger_array) > 1:
        next_round = []
        for i in range(0, len(challenger_array), 2):
            if challenger_array[i] > challenger_array[i + 1]:
                next_round.append(challenger_array[i])
            else:
                next_round.append(challenger_array[i + 1])
        challenger_array = next_round

    second_largest = challenger_array[0]

    return second_largest


# Example
arr = [10, 5, 7, 2, 9, 1, 15, 8]
second_largest = find_second_largest(arr)
print("Second largest number:", second_largest)

#Q2: You are a given a unimodal array of n distinct elements, 
#    meaning that its entries are in increasing order up until its maximum element,
#    after which its elements are in decreasing order. Give an algorithm to compute the maximum element that runs in O(log n) time.

def find_maximum(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]
        elif arr[mid - 1] > arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    # Error condition: Array is not unimodal
    return None

# Example usage
arr = [2, 5, 9, 12, 15, 7, 3, 1]
maximum = find_maximum(arr)
print("Maximum element:", maximum)
