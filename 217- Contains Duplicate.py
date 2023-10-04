class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Values = set()
        for num in nums:
            if num in Values:
                return True
            Values.add(num)
        return False
