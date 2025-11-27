class EmailValidator:
    def __init__(self, email):
        self.email = email
        
    @staticmethod
    def is_valid_email(email):
        return "Email is Valid" if "@" in email else "Invalid Email"
    
result = EmailValidator.is_valid_email("test@gmail.com")
result_invalid = EmailValidator.is_valid_email("test#gmail.com")
print(result)
print(result_invalid)