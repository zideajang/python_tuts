



class Solution:

    def __init__(self,nums):
        self.nums =nums

    def lomuto_partition(self,low,high):
        pivot = self.nums[high]

        i = (low - 1)
        for j in range(low, high):
            if (self.nums[j] <= pivot):
                i += 1
                self.nums[i],self.nums[j] = self.nums[j],self.nums[i]
            self.nums[i+1],self.nums[high] = self.nums[high],self.nums[i+1]
            return (i+1)
    
    def quickSort3(self,low,high):
        if( low < high):
            pi = self.lomuto_partition(low,high)

            self.quickSort3(low, pi-1)
            self.quickSort3(pi+1 ,high)

            print(self.nums)

    def quickSort2(self,nums):
        if len(nums)<=1: return nums

        smaller,equal,lager = [],[],[]
        pivot = nums[0]

        for x in nums:
            if x < pivot: smaller.append(x)
            elif x == pivot: equal.append(x)
            else: lager.append(x)
        return self.quickSort2(smaller) + equal + self.quickSort2(lager)

    def quickSort(self,nums,left,right):
        if (left >= right):
            return
        p = nums[left]
        i = left
        j = right
        while (i != j):
            while (j > i) and nums[j] > p:
                j -= 1
            nums[i],nums[j] = nums[j],nums[i]
            while (i < j) and nums[i] <= p:
                i += 1
            nums[i],nums[j] = nums[j],nums[i]
        self.quickSort(nums,left,i-1)
        self.quickSort(nums,i+1,right)
        # print(nums)
        
    def quickArraySort(self,nums):
        left = 0
        right = len(nums) - 1
        self.quickSort(nums,left,right)

if __name__ == "__main__":
    arr = [21,38,29,17,4,25,11,32,9]
    solution = Solution(arr)
    solution.quickSort3(0,len(arr)-1)
