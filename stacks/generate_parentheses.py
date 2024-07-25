# my javascript solution

# var generateParenthesis = function(n) {
#     const result = []
#     const stack = []

#     function backtrack(openCount, closeCount) {
#         if(openCount == n && closeCount === n) {
#             result.push(stack.join(""))
#             return 
#         }
#         if(openCount < n) {
#             stack.push("(")
#             backtrack(openCount + 1, closeCount)
#             stack.pop()
#         }
#         if(closeCount < openCount) {
#             stack.push(")")
#             backtrack(openCount, closeCount + 1)
#             stack.pop()
#         }
#     }

#     backtrack(0, 0)
#     return result
# };


# neetcode python solution

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