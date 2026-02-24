# Parent Class
class Electronic:
    brand = "ASUS"
    def power_on(self):
        print("Device is booting up...")

# Child Class inherits from Electronic
class Laptop(Electronic):
    model = "Vivobook"

my_laptop = Laptop()
my_laptop.power_on() # Accessing parent function
print(f"{my_laptop.brand} {my_laptop.model}")