laptops=["lenovo","dell","hp","asus","acer"]
for i,l in enumerate(laptops,start=1):
    print(f"{i}:{l}")
remove=int(input("enter the number of the laptop brand u want to remove"))
laptops.pop(remove-1)
print("Success! Brand removed.")
print(f"Final List: {laptops}")