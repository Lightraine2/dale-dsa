"""
Simple, in place sorting algorithm.
O(n2) time complexity due to nested loops. This is slow.
Python's sorted() is O(n log n) time complexity.
Space complexity is O(1) due to sorting in place, no new lists etc.
Not stable due to equal elements potentially being sorted out of order.

"""

def quicksort(array: list) -> list:
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    return array