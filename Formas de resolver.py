
#Factorial whit recursive mode
def factorialR (num):
    if num == 0:
        return 1
    else:
        return num * factorialR(num-1)


#Factorial whit iterative mode
def factorialI (num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial*i
    return factorial


#Fibonacci whit recursive mode
def fibonacciR (num):
    if (num == 0 or num == 1):
        return num
    else:
        fib=fibonacciR(num-1)+fibonacciR(num-2)
    return fib
        