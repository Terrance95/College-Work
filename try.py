class Hacker(Member):
    def __init__(self, name, role):
        super().__init__(name)
        self.role = role
        self.skills = []

    def add_skill(self, skill_name):
        self.skills.append(skill_name)
        print(f"Added {skill_name}")

    def remove_skill(self, skill_name):
        # Traditional way would crash if skill isn't found
        # Pro way: Try to remove, but don't panic if it's not there
        try:
            self.skills.remove(skill_name)
            print(f"Removed {skill_name} from profile.")
        except ValueError:
            print(f"Error: {skill_name} not found in your skill list!")

    def show_profile(self):
        print(f"\n--- {self.name.upper()}'S HACKER PROFILE ---")
        for i, s in enumerate(self.skills, start=1):
            print(f"{i}. {s}")

# Testing your new logic
user1 = Hacker("Terrance", "Logic Specialist")
user1.add_skill("Python")
user1.remove_skill("Java")  # This would normally crash, but now it's safe!
user1.show_profile()