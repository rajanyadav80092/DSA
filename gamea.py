game=input("enter your intrest")
while game!="b":
    name=int(input("enter a number : "))
    if name%2==0:
        print((name//2)+1)
        game=input("enter your intrest : ")
    else:
        print((name//2))
        game=input("enter your intrest : ")
print("thank to visit this webpage")