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

user_json = {
    "name" : "Aditya Saputra",
    "age" : 25,
    "email" : "aditya@example.com"
}

class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        
    @classmethod
    def from_json(cls, data):
        if not data:
            raise ValueError("Data json is empty")
        
        return cls(
            data.get("name"),
            data.get("age"),
            data.get("email")
        )
        
user = User.from_json(user_json)

width = 40
print("=" * width)
print(" Biodata ".center(width, "="))
print("=" * width)
print(f"{'Name':<10}: {user.name}")
print(f"{'Age':<10}: {user.age} years")
print(f"{'Email':<10}: {user.email}")
print("=" * width)
print()