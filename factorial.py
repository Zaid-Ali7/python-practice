def factorial(n):
    if n< 0:
        return f"factorial does not exist for negetive numbers"
    elif n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))