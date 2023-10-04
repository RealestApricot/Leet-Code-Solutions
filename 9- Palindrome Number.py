class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x != 0):
            return False
        FlippedNum = 0
        while x > FlippedNum:
            FlippedNum = FlippedNum*10 + x%10
            x //= 10
        return (FlippedNum == x) or (FlippedNum//10 == x)