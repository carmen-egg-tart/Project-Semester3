def factorial(n):
    # Check whether it is a non-negative integer
    if n < 0:
        return "Factorial cannot be used for negative numbers"
    elif n == 0 or n == 1:
        return 1
    
    result = 1
    # Calculate the factorial using a while loop
    while n > 1:
        result *= n
        n -= 1
    return result


number = int(input("Please enter a non-negative integer: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
