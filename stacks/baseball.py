from typing import List


def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b)
                stack.append(a)
                stack.append(a + b)
            elif operation == 'D':
                stack.append(stack[-1] * 2)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))

        return sum(stack)