class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def GetStack(Str):
            Stack = []
            for char in Str:
                if char == "#" and len(Stack) > 0:
                    Stack.pop()
                elif char != "#":
                    Stack.append(char)
            return Stack
        return GetStack(s) == GetStack(t)
