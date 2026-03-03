def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    
    # Calculate sum of digits raised to the power of total digits
    total_sum = sum(int(digit) ** num_digits for digit in num_str)
    
    return total_sum == n

# Test
val = int(input("Enter number to check Armstrong: "))
if is_armstrong(val):
    print("It is an Armstrong Number")
else:
    print("Not an Armstrong Number")