# Find the First True in a Sorted Boolean Array of the right section, i.e., the index of the first true element. 
# If there is no true element, return -1.

from typing import List

def find_boundary(arr: List[bool]) -> int:
    left = 0
    right = len(arr) - 1
    boundary_index = -1 
    while left <= right: 
        mid = (left + right) // 2 
        if arr[mid]:  
            boundary_index = mid
            right= mid - 1 
        else:
            left = mid + 1
    return boundary_index