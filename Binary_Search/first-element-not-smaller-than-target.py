# Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that 
# is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number
from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    left =   0
    right = len(arr) -1
    cur_idx = -1
    while left <= right: 
        mid = (left+right) //2 
        if arr[mid] >= target:
            right = mid - 1 
            cur_idx = mid
        else: 
            left = mid + 1
    return 
if __name__ == "__main__":
    arr = [1,3,3,5,8, 8, 10]
    target = 9

    res = first_not_smaller(arr, target)
    print(res)