class student:
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll

    def display(self):
        print(f"Student:{self.name}  | Roll Number:{self.roll}")

s1=student("terrance",95)
s1.display()