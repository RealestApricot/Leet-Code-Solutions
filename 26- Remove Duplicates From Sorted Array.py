class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i< len(nums):
            if i > 0 and nums[i] == nums[i-1]:
                nums.pop(i)
                i -= 1
            i += 1
        
        