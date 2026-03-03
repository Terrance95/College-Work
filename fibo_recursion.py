def fibo_recursive(n):
    # Base Case: The logic stops here
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive Case: The function calls itself
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)

# Contest Tip: Recursive calls are slow for large N (like N > 30).
# Only use this if the question specifically asks for "Recursion."
num = int(input("Enter term for Fibonacci: "))
print(f"Result: {fibo_recursive(num-1)}")