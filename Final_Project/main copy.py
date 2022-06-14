
from user import *
from food import *
from admin import *
# from main import *

while(True):
    login_type=int(input("Enter log_in type\n1 for admin login\n2 for user login\n3 to exit\n"))
    if login_type==1:
        admin_obj=Admin()

        id=input("enter admin username: ")
        if id in admin_obj.admin_creds.keys():
            password=input(f"enter password for {id}: ")
            if admin_obj.admin_creds[id]==password:
                print('log in successful')
                admin_obj.execute()
    elif login_type==2:
        while(True):
            print("1 to register\n2 to login\n3 to exit\nenter your choice:")
            choice=int(input())
            if choice==1 or choice==2:
                user_obj=User()
                user_obj.execute(choice)
            elif choice==3:
                break 

            else:
                print("invalid choice")
    elif login_type==3:
        break
    else:
        print("Invalid Choice, exiting the app")
