import math

def check_prime(n):
    # Step 1: Handle numbers less than 2
    if n < 2:
        return False
    
    # Step 2: Check 2 separately (optional but faster)
    if n == 2:
        return True
    
    # Step 3: Eliminate all even numbers early
    if n % 2 == 0:
        return False

    # Step 4: The Loop (Check from 3 to sqrt(n), skipping even numbers)
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 1)34:
        if n % i == 0:
            return False
            
    return True

# Testing the logic
num = int(input("Enter number for tomorrow's contest: "))
if check_prime(num):
    print(f"{num} is a PRIME number.")
else:
    print(f"{num} is NOT a prime number.")