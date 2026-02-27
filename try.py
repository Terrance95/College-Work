class Member:
    def __init__(self, name):
        self.name = name  # The "ID Card"
        print(f"Member {self.name} registered.")

class Hacker(Member):
    def __init__(self, name, role):
        # super() is the "Registration Clerk" 
        # It sends the 'name' to the Member class (just like C++)
        super().__init__(name) 
        self.role = role
        self.skills = []  # The "Backpack" (Vector)

    def add_skill(self, skill):
        self.skills.append(skill) # Same as push_back
        print(f"Added {skill}")

    def remove_skill(self, skill):
        # In C++ we used 'find' and 'erase'. 
        # In Python, we use 'if skill in list' and 'remove'.
        if skill in self.skills:
            self.skills.remove(skill)
            print(f"Removed {skill}")
        else:
            print(f"Error: {skill} not found!")

    def show(self):
        print(f"\n--- {self.name}'s Profile ---")
        # Enumerate gives the index (i) and value (s)
        for i, s in enumerate(self.skills, start=1):
            print(f"{i}. {s}")

# Execution
h = Hacker("Terrance", "Logic Specialist")
h.add_skill("Python")
h.add_skill("C++")
h.remove_skill("Java") # Shows error
h.show()