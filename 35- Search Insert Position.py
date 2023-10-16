class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def RecursiveSearch(nums: List[int], target: int, targetPosition: int):
            if not nums:
                return targetPosition
            mid = len(nums)//2
            if nums[mid] < target:
                return RecursiveSearch(nums[mid+1:], target, targetPosition + mid + 1)
            elif nums[mid] > target:
                return RecursiveSearch(nums[:mid], target, targetPosition)
            else:
                return targetPosition + mid
        return RecursiveSearch(nums, target, 0)
