class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for index in range(len(nums)):
            comparison = nums[len(nums)-1-index]
            if comparison >= goal - (len(nums)-1-index):
                goal = len(nums)-1-index
        return goal == 0