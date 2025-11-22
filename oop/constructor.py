class Biodata:
    name = ""
    age = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # String representation method
    def __str__(self):
        return f"Biodata(Name: {self.name}, Age: {self.age})"
        
biodata = Biodata("Aditya Saputra", 25)
print("=== Biodata Information ===")
print(f"Name: {biodata.name}")
print(f"Age: {biodata.age}\n")

print(biodata)  # Using __str__ method
print()

# Validating the constructor
class Person:
    name = ""
    age = 0
    
    def __init__(self, name, age = 17):
        if age <= 17:
            raise ValueError("Age must be greater than 17")
        
        self.name = name
        self.age = age
        
    def __eq__(self, value):
        return self.name == value.name and self.age == value.age
        
person = Person("Rina Wijaya", 22)
print("=== Person Information ===")
print(f"Name: {person.name}")
print(f"Age: {person.age}\n")   

person2 = Person("Rina Wijaya", 22)
print("Are person and person2 equal?", person == person2)  # Testing __eq method
print()

# Testing invalid age
# person_invalid = Person("Budi Santoso", 15)  # This will raise a ValueError
# print("=== Person Information ===")
# print(f"Name: {person_invalid.name}")
# print(f"Age: {person_invalid.age}\n")