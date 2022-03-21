class Solution(object):
    def maximumSubArray(self, arr):
        local_maximum = [arr[0]]
        n = len(arr)

        for i in range(1, n):
            print(i)
            local_maximum.append(max(arr[i], arr[i] + local_maximum[i - 1]))

        print(local_maximum)


Solution().maximumSubArray([1, -1, 3, 4, -3, 5])
