class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []

        def Addition(num1, num2):
            return num1 + num2

        def Subtraction(num1, num2):
            return num1 - num2

        def Multiplication(num1, num2):
            return num1 * num2

        def Division(num1, num2):
            return int(num1 / num2)

        def GetTopOfStack():
            return values[len(values)-2], values[len(values)-1]

        def ClearTopOfStack():
            values.pop(len(values)-1)
            values.pop(len(values)-1)

        operators = {
            "+": Addition,
            "-": Subtraction,
            "*": Multiplication,
            "/": Division,
        }

        for i in range(len(tokens)):
            if tokens[i] in operators:
                num1, num2 = GetTopOfStack()
                ClearTopOfStack()
                values.append(operators[tokens[i]](num1, num2))
            else:
                values.append(int(tokens[i]))
        return values[len(values)-1]
