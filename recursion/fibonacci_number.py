def fib(self, n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    return self.fib(n - 1) + self.fib(n - 2)

def fib_iterative(n):
    first_num = 0
    second_num = 1

    for i in range(2, n + 1):
        sum_num = first_num + second_num
        first_num = second_num
        second_num = sum_num
    
    return second_num

print(fib_iterative(100))