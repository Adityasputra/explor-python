class Math:
    
    @staticmethod
    def add(a, b):
        return a + b
    

# print(Math.add(2, 2)) # Result 4

class BankAccount:
    no = ""
    balance = 0
    active = True
    
    def __init__(self, no, balance = 0):
        self.no = no
        self.balance = balance
        
    @classmethod
    def disable(cls, no, balance = 0):
        result = cls(no, balance)
        result.active = False
        return result
    
User1 = BankAccount("1", "2000")
print("="*35)
print(f"No\t: {User1.no}\nBalance\t: {User1.balance}\nActive\t: {"This account is active" if User1.active else "This account is inactive"}")
print("="*35)

print()

User2 = BankAccount.disable("2", "5000")
print("="*35)
print(f"No\t: {User2.no}\nBalance\t: {User2.balance}\nActive\t: {"This account is active" if User2.active else "This account is inactive"}")
print("="*35)

print()

# Study Case Instance Method
class Rectangle:
    def __init__(self, s, d):
        self.s = s
        self.d = d
        
    def area_formula(self):
        return self.s ** 2
    
    def circumference_formula(self):
        return 4 * self.s
    
    def formula_area_of_a_diagonal(self):
        return (self.d ** 2) / 2
    
task1 = Rectangle(2, 2)
print(task1.area_formula())
print(task1.circumference_formula())
print(task1.formula_area_of_a_diagonal())

