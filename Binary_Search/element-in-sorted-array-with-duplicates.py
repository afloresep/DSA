# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. 
# Return -1 if the target is not in the array.

from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    left, right = 0, (len(arr) - 1)
    cur_idx = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
             cur_idx = mid
             right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
         
    return cur_idx 

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)

    [2, 3, 5, 7, 7, 7, 7,  11, 13, 17, 19]