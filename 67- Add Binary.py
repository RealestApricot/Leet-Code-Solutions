class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def Base10(num):
            sum = 0
            position = 0
            for digit in num[::-1]:
                sum += int(digit) * (2**position)
                position += 1
            return sum

        def Base2(num):
            if num == 0:
                return "0"
            binary = ""
            while num > 0:
                binary = str(num % 2) + binary
                num = num//2
            return binary
        return Base2(Base10(a)+Base10(b))
