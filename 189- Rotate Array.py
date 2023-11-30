class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        shiftAmount = k % len(nums)
        array1 = nums[:len(nums)-shiftAmount]
        array2 = nums[len(nums)-shiftAmount:]
        nums[:] = array2 + array1