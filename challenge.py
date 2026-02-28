sentence=input("enter a sentence:")

sentence=sentence.split()
count=len(sentence)
reverse=[w[::-1] for w in sentence]
reverse=" ".join(reverse) 
print(f"reversed sentence with the words in the same order:{reverse}")
print(F"number of words in the sentence:{count}")