# game=input("enter your intrest")
# while game!="b":
#     name=int(input("enter a number : "))
#     if name%2==0:
#         print((name//2)+1)
#         game=input("enter your intrest : ")
#     else:
#         print((name//2))
#         game=input("enter your intrest : ")
# print("thank to visit this webpage")

def substring(nums,k):
    right=len(nums)-1
    count=0
    for right in range(k):
        count+=1
    max_count=count
    for i in range(k,right):
        count+=1
        
        