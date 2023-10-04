class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        maxCount = 0
        maxIndex = 0
        nums.sort()
        if len(nums) == 1 or len(nums) == 2:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] != nums[right] or i == len(nums)-1:
                print(nums[left:right])
                if maxCount < len(nums[left:right]):
                    maxCount = len(nums[left:right])
                    maxIndex = nums[right]
                left = right
            right = i

        return maxIndex
