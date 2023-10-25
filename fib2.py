### Thomas Silva
### ENGR 103 project 4b.


def fib(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, num+ 1):
        a, b = b, a + b

    return b

# Test the function
print(fib(1))  # Output: 1
print(fib(3))  # Output: 2
print(fib(1000)) # Output: 55
