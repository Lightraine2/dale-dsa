"""
Time complexity: O(n²) in worst and average cases, O(n) in best case (with early exit optimization)
Space complexity: O(1) since it's in-place
Stability: Stable sort (maintains relative order of equal elements)

Not good, only worthwhile in small, almost sorted lists.
Could argue that in very space constrained situations, it could be used due to the O(1) space complexity and is a stable sort.
"""

def bubblesort(array: list) -> list:
    n = len(array)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
    return array