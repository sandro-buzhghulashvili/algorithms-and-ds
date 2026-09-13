from typing import List


def calPoints(self, operations: List[str]) -> int:
        recordStack = []
        for operation in operations:
            if operation == 'C':
                recordStack.pop()
            elif operation == 'D':
                recordStack.append(recordStack[-1] * 2)
            elif operation == '+':
                recordStack.append(recordStack[-1] + recordStack[-2])
            else:
                recordStack.append(int(operation))
        sum = 0
        for score in recordStack:
            sum += (score)
        return sum
