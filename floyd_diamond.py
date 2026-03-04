def print_diamond(n):
    # --- PART 1: UPPER TRIANGLE ---
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print numbers (Floyd style)
        for j in range(1, i + 1):
            print(j, end=" ")
        print() # New line after each row

    # --- PART 2: LOWER TRIANGLE (The Mirror) ---
    for i in range(n - 1, 0, -1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Test for the contest
rows = int(input("Enter number of rows for the top half: "))
print_diamond(rows)