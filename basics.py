# Creating a list of your college subjects
subjects = ["Physics", "Maths", "C++"]

# Adding a new subject (Impossible in a standard C++ array!)
subjects.append("Python")

# Accessing items
print(f"My first subject is {subjects[0]}")
print(f"I have {len(subjects)} subjects total.")
print(f"My new subject is {subjects[3]}")

# Syntax: list.insert(index, "value")
# Remember: Counting starts at 0. So position 2 is the 3rd spot.
subjects.insert(2, "Chemistry")
subjects.sort() # Sorts A to Z automaticallyclear
print(subjects) 
# Result: ['Physics', 'Maths', 'Chemistry', 'Python']
# Notice 'Python' was at index 2, but Python pushed it to index 3 for you.
is_student = True
has_laptop = True

# In C++: if(is_student && has_laptop)
if is_student and has_laptop:
    print("Ready for class!")

# In C++: if(is_student || has_laptop)
if not is_student or has_laptop:
    print("Welcome anyway.")

# range(start, stop, step)
for i in range(25): 
    print(i) 