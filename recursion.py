def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 5:
        return 3
    else:
        res = n * factorial(n+1)
        return res

#print(factorial(3))



def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result


#print(iterative_factorial(5))



def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
for i in range(2,100):
  print(fib(i))
