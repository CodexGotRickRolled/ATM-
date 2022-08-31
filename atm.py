class ATM(object):
    balance=5000
    def login(self,pin):
        if pin==1234:
            return True
        else:
            return False
    def credit(self,amt):
        self.balance+=amt
    def debit(self,amt):
        self.balance-=amt
    def display(self):
        print("Your balance is "+str(self.balance))
obj=ATM()
flag=False
for i in range(1,4):
    if obj.login(int(input("enter the  pin"))):
       flag=True
       break
if flag:
    while True:
        o=input("Press C for credit and D for debit")
        if o=="D" or o=="d":
            amt=int(input("Enter the Amount"))
            if amt<obj.balance:
                obj.debit(amt)
                obj.display()
            else:
                print("Insufficient Balance")
        elif o=="C" or o=="c":
            amt=int(input("Enter the Amount"))
            obj.credit(amt)
            obj.display()

        
        
    
    
    
        
