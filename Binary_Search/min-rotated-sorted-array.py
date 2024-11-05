# A sorted array of unique integers was rotated at an unknown pivot. 
# For example, [10, 20, 30, 40, 50] becomes [30, 40, 50, 10, 20]. 
# Find the index of the minimum element in this array.
# Input: [30, 40, 50, 10, 20]
# Output: 3
# Explanation: The smallest element is 10, and its index is 3o


from typing import List 

def find_min_rotated(arr: List[int]) -> int:
    left, right = 0, len(arr) - 1
    cur_idx = 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= arr[right]:
            right = mid -1 
            cur_idx = mid
        else:
            left = mid +1

        return cur_idx
    