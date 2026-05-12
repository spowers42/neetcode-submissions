from collections import deque


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            match token:
                case "+":
                    r2 = stack.pop()
                    r1 = stack.pop()
                    stack.append(r1 + r2)
                case "-":
                    r2 = stack.pop()
                    r1 = stack.pop()
                    stack.append(r1 - r2)
                case "*":
                    r2 = stack.pop()
                    r1 = stack.pop()
                    stack.append(r1 * r2)
                case "/":
                    r2 = stack.pop()
                    r1 = stack.pop()
                    stack.append(int(r1 / r2))
                case _:
                    stack.append(int(token))

        return stack[0]
