import re
from user import *
from food import *
from admin import *
# from main import *
class Main:

    user_list=[]

    def admin_login(self):
        id=input("enter admin id: ")
        if id =='admin':
            password=input(f"enter password for {id}: ")
            if password== 'admin':
                print('log in successful')
                admin_obj=Admin()
                admin_obj.execute()
            else:
                print("Invalid Password")
        else:
            print("invalid id")


    def email_validation(self,email):
        pattern='^\w+@[A-Za-z0-9]+.[A-Za-z0-9]+$'
        if re.match(pattern,email):
            return True
        else:
            return False


    def phone_validation(self,ph_no):
        pattern='^\d{10}$'
        if re.match(pattern,ph_no):
            return True
        else:
            return False


    def check_db(self,email):
        exists=False
        for user1 in self.user_list:
            if user1.email==email:
                exists=True
                break
        return exists


    def user_registration(self):
        user_details=dict()
        print('*********Registration*********\n\n')
        user_details['name']=input("Enter your full name: ")
        user_details['ph_no']=input("Enter your phone number(Valid 10-digit): ")
        user_details['email']=input("Enter a valid email (abc@def.com): ")
        user_details['address']=input("Enter your address: ")
        user_details['password']=input("enter a password: ")
        if not(self.phone_validation(user_details['ph_no'])):
            print(" invalid phone number")
            user_details= None
        elif not(self.email_validation(user_details['email'])):
            print(" invalid email")
            user_details= None
        elif self.check_db(user_details['email']):
            print("User already exists")
            user_details= None

        else:
            user_obj=User(**user_details)   
            self.user_list.append(user_obj)

    def user_menu(self,user_obj):
        
        
        while(True):
            
            message=str('*'*5+f'Welcome {user_obj.name}!'+'*'*5+'\nEnter your choice\n'+
                    '1 to Place New Order\n2 for Order History\n3 to Update Profile\n4 to logout\n')
            choice=int(input(message))
            if choice==1:
                user_obj.place_order()
            elif choice==2:
                user_obj.display_history()
            elif choice==3:
                while(True):
                    msg='Enter option to update:\n1 Name\n2 Phone Number\n3 Address\n4 Password\n5 Email\n6 All\n7 to exit\n'
                    try:
                        option=int(input(msg))
                    except:
                        print('enter a number')
                        break
                    if option==1:
                        user_obj.set_name(input('Enter new value: '))
                    elif option==2:
                        ph_no=input('Enter new 10-digit phone number: ')
                        if self.phone_validation(ph_no):
                            user_obj.set_ph_no(ph_no)
                        else:
                            print('invalid phone number')                
                    elif option==3:
                        user_obj.set_address(input('Enter new value: '))

                    elif option==4:
                        user_obj.set_password(input('Enter new value: '))
                    elif option==5:
                        email=input("Enter a valid email (abc@def.com): ")
                        if self.email_validation(email):
                            if self.check_db(email):
                                print('Email already registered to another user')
                            else:
                                user_obj.set_email(email)
                        else:
                            print('Invalid email id')
                    elif option==6:
                        user_details=user_obj.get_details()
                        if self.email_validation(user_details['email']):
                            if self.check_db(user_details['email']):
                                print('Email id already registered with another user')
                            
                            else:
                                if self.phone_validation(user_details['ph_no']):
                                    self.update_user(user_details)
                                    print("Updated Succesfully")
                                else:
                                    print('Invalid Phone Number')
                        else:
                            print('Invalid email id')
                    elif option==7:
                        break
                    else:
                        print('invalid choice')
                
            elif choice==4:
                break
            else:
                print("invalid choice")    
    
    def user_login(self):

        not_found=True
        email=input("Enter user email: ")
        if self.email_validation(email):
            for current_user in self.user_list:
                if current_user.email==email:
                    not_found=False
                    password=input("Enter Password: ")
                    if current_user.password==password:
                        welcome_message='*'*5+'log in successful'+'*'*2+'Welcome!'+'*'*5
                        print(welcome_message)

                        self.user_menu(current_user)

                        break
                    else:
                        print("Wrong Password")
                        break
            if not_found:
                print('User not found')    
        else:
            print('Invalid email, please enter a valid email id')
            
    
    def user_main_page(self):
        while(True):
            print("1 to register\n2 to login\n3 to exit\nenter your choice:")
            choice=int(input())
            if choice==1:
                self.user_registration()
            elif choice==2:
                self.user_login()
            elif choice==3:
                break 
            else:
                print("invalid choice")


while(True):
    login_type=int(input("Enter log_in type\n1 for admin login\n2 for user login\n3 to exit\n"))
    main_obj=Main()
    if login_type==1:
         main_obj.admin_login()  
    elif login_type==2:
        main_obj.user_main_page()
    elif login_type==3:
        break
    else:
        print('Invalid Package')

