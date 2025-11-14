def factorial(n):
    # Initialize result to 1
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result

sample_number = 10
output = factorial(sample_number)

print(f"The factorial of {sample_number} is {output}.")