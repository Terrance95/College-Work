import math

def is_strong(n):
    temp = n
    total_sum = 0
    
    # Extract digits one by one
    while temp > 0:
        digit = temp % 10          # Get the last digit
        total_sum += math.factorial(digit) # Add its factorial
        temp //= 10                # Remove the last digit
        
    return total_sum == n

# --- Test ---
num = 145
if is_strong(num):
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is NOT a Strong Number")