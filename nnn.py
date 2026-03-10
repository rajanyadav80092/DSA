# class BankAccount:
#     bankname="Bank of baroda"
#     all_account=[]
#     def __init__(self,name,number,balance):
#         self.name=name
#         self.__balance=balance
#         self.number=number
#         BankAccount.all_account.append(self)
        
   
#     def deposite(self,amount):
#         self.__balance+=amount
#         return f"deposite : {amount} total balance : {self.__balance}"
   
#     def withdrawan(self,amount):
#         if self.__balance<=amount:
#             return "please check bank balance"
#         else:
#             self.__balance-=amount
#             return f"withdrawan amount {amount} , total balance : {self.__balance}"
    
#     @property
#     def show_detail(self):
#         return f" balance: {self.__balance} name: {self.name} number: {self.number}"
#     @classmethod
#     def changebank(cls,new_name):
#         cls.bankname=new_name
#         return f"your new bank : {new_name}"
#     @classmethod
#     def show_all_bankaccount(cls):
#         print(f" your bank name : {cls.bankname}" )
#         for show in cls.all_account:
#             print(show.show_detail)
#     @staticmethod
#     def disclaimer():
#         return "you open account minimum amount is : 1000"

# acc1=BankAccount("rajan",123456,1000)
# acc2=BankAccount("vikash",123465,8000)
# acc3=BankAccount("prince",123564,10000)
# acc4=BankAccount("arpit",124563,1200)
# acc5=BankAccount("vipin",134562,150000)

# print(acc1.withdrawan(500))
# BankAccount.show_all_bankaccount()

def min_len_subay(arr,s):
    min_len=float("-inf")
    left=0
    curr=0
    
    for right in range(len(arr)):
        curr+=arr[right]
        
        while curr>=s:
            min_len=max(min_len,right-left+1)
            curr-=arr[left]
            left+=1
    return 0 if min_len == float("inf") else min_len
arr = [2, 1, 5, 2, 3, 2]
print(min_len_subay(arr,7))


