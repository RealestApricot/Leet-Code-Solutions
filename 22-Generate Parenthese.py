class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        Stack = []
        Results = []

        def MakeResults(OpenN, ClosedN):
            if OpenN == ClosedN == n:
                Results.append("".join(Stack))
                return
            if OpenN < n:
                Stack.append("(")
                MakeResults(OpenN + 1, ClosedN)
                Stack.pop()
            if ClosedN < OpenN:
                Stack.append(")")
                MakeResults(OpenN, ClosedN + 1)
                Stack.pop()
        MakeResults(0, 0)
        return Results