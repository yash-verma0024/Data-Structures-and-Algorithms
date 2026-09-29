class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        result = 0
        n = len(tokens)

        for i in range(n):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()
                if tokens[i] == "+":
                    result = a + b

                if tokens[i] == "-":
                    result = a - b

                if tokens[i] == "*":
                    result = a * b

                if tokens[i] == "/":
                    result = int(a / b)

                stack.append(result)
        return stack[-1]

    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

    print(evalRPN(tokens))