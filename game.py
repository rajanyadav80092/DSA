import random
option=["rock","paper","scissor"]
name=input("Enter your name : ")

user_win=0
comp_count=0
Tie=0


while True:
    data=input("Enter your choice play or break")
    if data=="break":
        break
    user=input("enter your choice: ")
    comp=random.choice(option)
    if user!="rock" and user != "scissor" and user != "paper":
        print()
        print("please enter correct data")
        user=input("Enter your choice: ")
        
    if user=="paper":
        if comp=="rock":
            print()
            print(f"user win user choice : {user} comp choice : {comp}")
            user_win+=1
        elif comp=="scissor":
            print()
            print(f"comp win choice {comp} user choice {user}")
            comp_count+=1
        else :
            print("Tie match")
            Tie+=1
    elif user=="rock":
        if comp=="paper":
            print()
            print(f"comp win choice {comp} user choice {user}")
            comp_count+=1
        elif comp=="scissor":
            print()
            print(f"user win user choice : {user} comp choice : {comp}")
            user_win+=1
        else:
            print("Tie match")
            Tie+=1
    else:
        if comp=="paper":
            print()
            print(f"user win user choice : {user} comp choice : {user}")
            user_win+=1
        elif comp=="rock":
            print()
            print(f"comp win choice {comp} user choice {user}")
            comp_count+=1
        else:
            print()
            print("Tie match")
            Tie+=1
    

print(f"THANK YOU : {name} ")
print("COMPUTER WIN COUNT : ",comp_count)
print()
print(f"{name} WIN COUNT: ",user_win)
print("MATCH DRAWN : ",Tie)
   
    
