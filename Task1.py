def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

sample = int(input("Enter a number: "))
result = factorial(sample)
print(f"The factorial of {sample} is {result}")
