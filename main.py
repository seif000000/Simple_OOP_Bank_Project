class Customer:
    def __init__(self,name,age,gander,contactno):
        self.name = name 
        self.age = age 
        self.gander = gander
        self.contactno = contactno
        
    def show_cust_details(self):
        print("Customer details are as follows ..... \n")
        print(f"name : {self.name} ")
        print(f"age : {self.age}")
        print(f"gandar : {self.gander}")
        print(f"contactno no : {self.contactno}")
        
        
class Bank(Customer):
    def __init__(self, name, age, gander, contactno):
        super().__init__(name, age, gander, contactno)
        self.balance = 0
        
    def deposit_transaction(self,amount):
        self.amount = amount
        self.balance += self.amount
        print(f"Your account balance is credited by Rs: {self.amount}")
        print(f"Your account balabce is Rs: {self.balance}")
        
    def withdraw_transaction(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print(f"sorry insufficient ! your avilable balance is {self.balance}")
        else:
            self.balance -=self.amount
            print(f"Your account balance is credited by Rs: {self.amount}")
            print(f"Your account balabce is Rs: {self.balance}")
            
    def check_balance(self):
        print(f"your available account is Rs: {self.balance}")
        
        
        
        
c1 = Bank("seif",20,"male",50241834)
c1.show_cust_details()
print("******************")
c1.deposit_transaction(25000)
print("******************")
c1.withdraw_transaction(15000)
print("******************")
c1.check_balance()
print("******************")
c1.show_cust_details()


