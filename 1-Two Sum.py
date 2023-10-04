class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Compliments = {}
        for i in range(len(nums)):
            Compliments[nums[i]] = target - nums[i]
        
        for i in range(len(nums)):
            Comp = Compliments[nums[i]]
            if Comp in nums and nums.index(Comp) != i:
                return [i, nums.index(Comp)]