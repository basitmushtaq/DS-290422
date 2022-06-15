

from admin import *
class User():
    def __init__(self,**user_details):
        self.name=user_details['name']
        self.ph_no=user_details['ph_no']
        self.email=user_details['email']
        self.address=user_details['address']
        self.password=user_details['password']
        self.history=[]


    def place_order(self):
        admin_obj=Admin()
        self.food_list=admin_obj.get_food_list()
        if self.food_list:
            for i,food_item in enumerate(self.food_list):
                print(f'{i}. {food_item.get_name()} ({food_item.get_quantity()}) [{food_item.get_price()}]')
            choice=list(map(int,input("Enter choices separated by comma(,): ").split(',')))
            print(choice)
            food_choice=[self.food_list[i] for i in choice]
            print('*****Your order****')
            discount=0
            actual_price=0
            for item in food_choice:
                actual_price+=item.get_price()
                discount+=item.get_discount()
                print(f'{i}. {item.get_name()} ({item.get_quantity()}) [{item.get_price()}]')
            print(f"Total payable amount = {actual_price}\nDiscount = {discount}\nFinal price = {actual_price-discount}")
            confirm=int(input('Enter 1 to comfirm order any other key to cancel: '))
            if confirm==1:
                self.history.append(food_choice)
                for item in food_choice:
                    id=item.food_id
                    admin_obj.update_inventory(id)
                print('Order placed\n\n')
        else:
            print("No food availabe, try again soon")


    def display_history(self):
        history=self.history
        if history:
            for i,item in enumerate(history):
                print(f'Order no.{i+1} :')
                for food_obj in item:
                    print(f'Name    :\t{food_obj.get_name()}')
        else:
            print('No records Found')



    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
    def set_email(self,email):
        self.email=email
    def get_email(self):
        return self.email
    def set_ph_no(self,ph_no):
        self.ph_no=ph_no
    def get_ph_no(self):
        return self.ph_no
    def set_address(self,address):
        self.address=address
    def get_address(self):
        return self.address
    def set_password(self,password):
        self.password=password
    def get_history(self):
        return self.history
    def set_history(self,history):
        self.history+=history
    

    def update_user(self,**user_dict):
        self.name=user_dict['name']
        self.ph_no=user_dict['ph_no']
        self.email=user_dict['email']
        self.address=user_dict['address']
        self.password=user_dict['password']

    def get_details(self):
        user_dict=dict()
        user_dict['name']=input("Enter your full name: ")
        user_dict['ph_no']=input("Enter your phone number(Valid 10-digit): ")
        user_dict['address']=input("Enter your address: ")
        user_dict['password']=input("enter a password: ")
        user_dict['email']=input("Enter a valid email (abc@def.com): ")
        return user_dict        

        

            



