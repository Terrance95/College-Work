word = "University"

# 1. Reverse the string (The most common contest trick)
reversed_word = word[::-1] 

# 2. Get the first 4 letters
prefix = word[:4] # "Univ"

# 3. Get every second letter
skipped = word[::2] # "U i e s t"

print(f"Original: {word}\nReverse: {reversed_word}\nEvery 2nd: {skipped}\n first 4 letters : {prefix}")