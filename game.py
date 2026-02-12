import random
option=["rock","paper","scissor"]
name=input("Enter your name : ")

user_win=0
comp_count=0
Tie=0


while True:
    choice=input("enter play or break : ")
    if choice == "break" :
        break
    
    user=input("enter the option : ")
    comp=random.choice(option)
    if user!="paper" and user!="rock" and user!="scissor":
        print("put right thing to option you put wrong : ",user)
        user=input("enter the correct option : ")
    if user == comp :
        print(f"TIE : comp choice : {comp}")
        Tie+=1
        
    elif user == "rock" :
        if comp=="paper" :
            print(f"COMP WIN COMP CHOICE: {comp}")
            comp_count+=1
            
        elif comp == "scissor":
            print(f"{name} WIN COMP CHOICE : {comp}")
            user_win+=1
        
    elif user == "paper":
        if comp == "rock" :
            print(f"{name} WIN COMP CHOICE : {comp}")
            user_win+=1
          
        elif comp == "scissor":
            print(f"COMP WIN COMP CHOICE: {comp}")
            comp_count+=1
          
        
    elif user == "scissor":
        if comp == "rock":
            print(f"{name} WIN COMP CHOICE : {comp}")
            user_win+=1
        elif comp == "paper":
            print(f"COMP WIN COMP CHOICE : {comp}")
            comp_count+=1

print(f"THANK YOU : {name} ")
print("COMPUTER WIN COUNT : ",comp_count)
print()
print(f"{name} WIN COUNT: ",user_win)
print("MATCH DRAWN : ",Tie)
   
    
