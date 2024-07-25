def generateParenthesis(n):
    # only add open parenthesis if open < n
    # only add a closing parenthesis if closed < open
    # valid if open == closed == n
    stack = []
    res = []

    def backtrack(openCount, closedCount):
        if openCount == closedCount == n:
            res.append("".join(stack))
            return 
        if openCount < n:
            stack.append("(")
            backtrack(openCount + 1, closedCount)
            stack.pop()
        if closedCount < openCount:
            stack.append(")")
            backtrack(openCount, closedCount + 1)
            stack.pop()

    backtrack(0, 0)
    print(res)

generateParenthesis(3)


## res = ["((()))"]