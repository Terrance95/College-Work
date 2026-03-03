n=4
num=1
for i in range(26):
    print(" " * (n-i-1),end=" ")
    for j in range(i+1):
       print(chr(65 + i), end=" ")
    print()
