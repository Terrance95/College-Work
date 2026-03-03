def get_fibonacci(n):
    a = 0
    b = 1
    
    if n <= 0:
        return "Invalid Input"
    elif n == 1:
        return a
    elif n == 2:
        return b
    else:
        # We start from 3 because we already know the 1st and 2nd
        for i in range(3, n + 1):
            next_term = a + b
            a = b           # 'a' moves to the old 'b'
            b = next_term   # 'b' moves to the new sum
        return b
    
t = int(input())
for _ in range(t):
    n = int(input())
    print(get_fibonacci(n))

# Test for tomorrow
n_term = int(input("Which Fibonacci term do you want? "))
print(f"The {n_term}th term is: {get_fibonacci(n_term)}")
