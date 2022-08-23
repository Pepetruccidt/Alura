class  Account:
    def __init__(self, number, owner, funds, limit):
         self.__number = number
         self.__owner = owner
         self.__funds = funds
         self.__limit = limit
         
    def extract(self):
        print(f"The user has {self.__funds}")
        
    def deposit(self, value):
        self.__funds += value
         
    def withdraw(self, value):
        if (self.__enough_credit(value)):
            self.__funds -= value
        else:
            print("Not enough credit")
        
    def transfer(self, target_account, value):
        if (self.__enough_credit(value)):
            self.__funds -= value
            target_account.__funds += value
        else:
            print("Not enough credit")
            
    def __enough_credit(self,value):
        return self.__funds - value >= -self.__limit
        
            
    @staticmethod
    def bank_code():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
            
    @property
    def limit(self):
        return self.__limit
    
    @property
    def funds(self):
        return self.__funds
    
    @property
    def owner(self):
        return self.__owner
    
    @limit.setter    
    def limit(self, value): 
        self.__limit = value
        
        