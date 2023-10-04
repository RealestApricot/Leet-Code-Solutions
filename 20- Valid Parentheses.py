class Solution:
    def isValid(self, s: str) -> bool:
        Table = {
            ")" : "(",
            "]" : "[",
            "}" : "{",
        }
        Stack = []
        for char in s:
            if char in Table.values():
                Stack.append(char)
            elif char in Table.keys():
                if len(Stack) == 0 or Stack.pop() != Table[char]:
                    return False

        return len(Stack) == 0