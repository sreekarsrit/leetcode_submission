class Solution:
    def check(self, nums: List[int]) -> bool:
        drop=0
        for i in range(0,len(nums)): # we have to check with the last ele also 
            if nums[i - 1] > nums[i]:
                drop+=1
        return drop < 2