# My solution in JavaScript :

# var isValid = function(s) {
#     const validParentheses = {
#         "(" : ")",
#         "{" : "}",
#         "[" : "]"
#     }
#     const stack = []


#     for(let char of s) {
#         if(char in validParentheses) {
#             stack.push(char)
#         } else {
#             if(stack.length === 0 || validParentheses[stack.pop()] !== char) return false 
#         }
#     }


#     return stack.length === 0
# };

# Neetcode solution :

def isValid(s):
    stack = []
    closeToOpen = {
        ")" : "(",
        "}" : "{",
        "[" : "]"
    }

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else :
                return False
        else :
            stack.append(c)

    return True if not stack else False