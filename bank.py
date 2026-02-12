class BankAccount:
    bankname="Bank of baroda"
    All_Account=[]
    
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.__balance=balance
        BankAccount.All_Account.append(self)
        
        
    # METHOD in deposite account
    def deposite(self,amount):
        self.__balance+=amount
        print("deposite amount",amount,"was debited")
        
    #withdrawn in account
    def withdrawn(self,amount):
        self.__balance-=amount
        print("withdrwan amount",amount,"was credit")
    
    #Show details in one BankAccount
    @property
    def show_detail(self):
        return f"Name : {self.account_holder}, Balance : {self.__balance} Account_number : {self.account_number} "
    @classmethod
    def name(cls,new_name):
        cls.bankname=new_name
        return new_name
        
    @classmethod
    def show_all_accounts(cls):
        print(f"\nAll Accounts in {cls.bankname}:")
        for acc in cls.All_Account:
            print(acc.show_detail)
    
    #instance method
    @property
    def get_balance(self):
        return self.__balance
        
    @staticmethod
    def all():
        print("minimum amount required to 1000")
        
acc1=BankAccount("Rajan",123456,100)
acc2=BankAccount("Vipin",231456,1000)
acc3=BankAccount("Shubham",213465,500)
acc4=BankAccount("Arpit",123465,900)

acc2.deposite(600)
BankAccount.show_all_accounts()
