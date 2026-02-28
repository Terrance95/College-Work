sentence = "Python is better than C++"

# 1. Convert string to a List of words
words = sentence.split() # ['Python', 'is', 'better', 'than', 'C++']

# 2. Reverse the List
words.reverse()

# 3. Join them back into a string with spaces
final_sentence = " ".join(words)

print(final_sentence) # Result: "C++ than better is Python"