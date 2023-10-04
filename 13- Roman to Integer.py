class Solution:
    def romanToInt(self, s: str) -> int:
        RomanValues = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        Total = 0
        PreviousValue = 0

        for Numeral in reversed(s):
            Value = RomanValues[Numeral]
            if Value < PreviousValue:
                Total -= Value
            else:
                Total += Value
            PreviousValue = Value
        
        return Total