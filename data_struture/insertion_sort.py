class Solution:
    def insertionArraySort(self, nums):
        n = len(nums) 
        for i in range(1, n):
            j = i
            while nums[j-1] > nums[j] and j > 0:
                nums[j-1], nums[j] = nums[j],nums[j-1]
                j -= 1

        return nums

    def sellArraySort(self, nums):
        n = len(nums)
        gap = n // 2
        while gap > 0:
            for i in range(gap,n):
                anchor = nums[i]
                j = i
                while j>=gap and nums[j-gap] > anchor:
                    nums[j] = nums[j - gap]
                    j -= gap
                nums[j] = anchor
            gap = gap // 2
        return nums

if __name__ == "__main__":
    print("solution...")
    # arr = [2,1,3,5,5,6,9,8]
    arr = [21,38,29,17,4,25,11,32,9]

    solution = Solution()
    print(solution.sellArraySort(arr))

    for i in range(3,10):
        print(i)