class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return len(nums)
        
        count = 2
        
        for index in range(2, len(nums)):
            if nums[index] != nums[count - 2]:
                nums[count] = nums[index]
                count += 1
        
        return count
