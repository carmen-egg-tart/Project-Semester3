def factorial(n):
    # Check whether it is a non-negative integer
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    
    result = 1
    # Calculate the factorial using the for loop
    for i in range(2, n + 1):
        result *= i
    return result

number = int(input("Please enter a non-negative integer: "))
result = factorial(number)
print(f"The factorial of {number} is {result}")
