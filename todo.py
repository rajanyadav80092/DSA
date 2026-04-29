# def to_do_list():
#     tasks=[]
    
#     while True:
#         print("1. Add task")
#         print("2. Remove task")
#         print("3. show Task")
#         print("4. Quit")
        
#         choice=input("Enter your choice : ")
        
#         if choice=="1":
#             task=input("Enter your choice")
#             tasks.append(task)
#         elif choice=="2":
#             task=input("enter your task")
#             if task in tasks:
#                 tasks.remove(task)
#             else:
#                 print("task not found")
        
#         elif choice=="3":
#             for task in tasks:
#                 print("-"+task)
            
#         elif choice=="4":
#             break
#         else:
#             print("invalid choice")
# to_do_list()

a=int(input("enter your numebr"))

if a&1:
    print("odd")
else:
    print("even")
            