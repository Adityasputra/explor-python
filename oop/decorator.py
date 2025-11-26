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

