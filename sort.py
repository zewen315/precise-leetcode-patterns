import random
from typing import List


# | Algorithm      | Best       | Average    | Worst      | Stable |
# | -------------- | ---------- | ---------- | ---------- | ------ |
# | Bubble Sort    | O(n)       | O(n²)      | O(n²)      | ✅      |
# | Selection Sort | O(n²)      | O(n²)      | O(n²)      | ❌      |
# | Insertion Sort | O(n)       | O(n²)      | O(n²)      | ✅      |
# | Merge Sort     | O(n log n) | O(n log n) | O(n log n) | ✅      |
# | Quick Sort     | O(n log n) | O(n log n) | O(n²)      | ❌      |
# | Heap Sort      | O(n log n) | O(n log n) | O(n log n) | ❌      |


# Bubble Sort
def bubbleSort(nums: List[int]) -> None:
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:  # already sorted, stop early
            break
    
    print(nums)

# Selection Sort

# Insertion Sort

# Merge Sort

# Quick Sort

# Heap Sort

# Bucket sort


def _randomNums(length: int) -> None:
    if length <= 0:
        return []

    nums = list(range(length))
    random.shuffle(nums)

    return nums


if __name__ == "__main__":
    nums = _randomNums(20)

    bubbleSort(nums.copy())