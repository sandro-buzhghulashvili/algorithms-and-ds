## My O(n^2) approach in JavaScript:

# var dailyTemperatures = function(temperatures) {
#     const answer = new Array(temperatures.length).fill(0);


#     for(let temp in temperatures) {
#         let count = 0
#         for(let i = temp; i < temperatures.length; i++) {
#             if(temperatures[i] > temperatures[temp]) {
#                 answer[temp] = count
#                 count = 0
#                 break;
#             } else {
#                 count += 1
#             }
#         }
#     }

#     console.log(answer)
#     return answer
# };

## Neetcode - O(n) monotioc decreasing stack

def dailyTemperatures(temperatures):
    res = [0] * len(temperatures)
    stack = [] # pair : [temp, index]

    for i, t in enumerate(temperatures):
        while stack and t > stack[-1][0]:
            stackT, stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append([t, i])
    
    return res