my_tasks=["study","workout","sleep"]
new=input("enter the new task")
my_tasks.insert(0,new)
my_tasks.sort()
for index, task in enumerate(my_tasks):
    print(f"{index + 1}. {task}")