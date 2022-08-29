class Checking_Account:
    
    def __init__(self, code):
        self.code = code
        self.available = 0
        
    def deposit(self, value):
        self.available += value
    
    def __str__(self) -> str:
        return f"[>> Code {self.code}, Available {self.available}<<]"
    
    
account1 = Checking_Account(23)
account1.deposit(100)
print(account1)
    