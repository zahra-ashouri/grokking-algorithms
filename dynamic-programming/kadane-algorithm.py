"""
find the largest possible sum of a contiguous sub-array within a given array
leetcode problem:
https://leetcode.com/problems/maximum-subarray/
"""

if __name__ == "__main__":

    # arr = [3, 1, 12, 5, 100, 10]
    arr = [-2, 3, -5, 2, 2, -1, 4, -3]
    n = len(arr)
    global_max = arr[0]
    local_max = arr[0]
    for i in range(1, n):
        local_max = max(arr[i], arr[i] + local_max)
        global_max = max(global_max, local_max)

    print(global_max)
