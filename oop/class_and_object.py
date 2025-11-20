class University:
    # Class Attributes
    name = ""
    location = ""
    established_year = 0
    
    def display_info(self, name):
        if not name:
            name = self.name
            
        print(f"University Name: {name}")
        print(f"Location: {self.location}")
        print(f"Established Year: {self.established_year}")
        

class Student:
    # Class Attributes
    first_name = ""
    last_name = ""
    age = 0
    major = ""


university = University()
student = Student()

# Instance Attributes
university.name = "Tech University"
university.location = "Cityville"
university.established_year = 1965

student.first_name = "Alice"
student.last_name = "Johnson"
student.age = 20
student.major = "Computer Science"

# Displaying University Information
# print("=== University Information ===")
# print(f"Name: {university.name}")
# print(f"Location: {university.location}")
# print(f"Established Year: {university.established_year}\n") 

# Displaying Student Information
# print("=== Student Information ===")
# print(f"First Name: {student.first_name}")
# print(f"Last Name: {student.last_name}")
# print(f"Age: {student.age}")
# print(f"Major: {student.major}\n")

# Using Method to Display University Info
print("=== University Information (Using Method) ===")
university.display_info("Global Tech University")