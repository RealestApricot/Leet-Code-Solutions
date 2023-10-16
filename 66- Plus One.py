class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[len(digits)-1] += 1
        increase = 0
        for i in range(len(digits)-1, -1, -1):
            digits[i] += increase
            increase = 0
            if digits[i] == 10:
                digits[i] = 0
                increase = 1
        if increase > 0:
            digits.insert(0, increase)
        return digits
