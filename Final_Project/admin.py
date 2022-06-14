
from food import *
class Admin():
    star='*'
    food_list=[]

    
    def get_food_list(self):
        return self.food_list

    def update_inventory(self,id):
        for food_item in self.food_list:
            if food_item.food_id==id:
                if food_item.stock<2:
                    self.food_list.remove(food_item)
                else:
                    food_item.stock-=1

    def display_menu(self):
        
        print(f'{self.star*10}Welcome to admin section{self.star*10}\n1 to add new food item\n2 to edit food item\n3 to view all food list\n4 to delete food item\n5 to logout\nEnter your choice: ')
    
    def get_details(self):
        
        food_dict=dict()
        
        food_dict['name']=input("Enter food name: ")
        food_dict['quantity']=input("Enter Quantity: ")
        food_dict['price']=float(input("Enter Price: "))
        food_dict['discount']=float(input("Enter Discount: "))
        food_dict['stock']=int(input("Enter Stock quantity: "))
        return food_dict


        
       

    def execute(self):
        while (True):
            self.display_menu()
            choice=int(input())
            if choice==1:
                print(f'{self.star*10} Add Food Item {self.star*10}')
                food_dict=self.get_details()
                if self.food_list==[]:
                    food_dict['id']=1
                else:
                    food_dict['id']=self.food_list[-1].food_id + 1

                food_obj=Food(**food_dict)
                self.food_list.append(food_obj)
                print(f'{self.star*3} Successful added with id {food_dict["id"]} {self.star*3}')
            elif choice==2:
                not_found=True
                print(f'{self.star*10} update food item {self.star*10}')
                food_id=int(input("enter food id: "))
                for food_obj in self.food_list:
                    if food_obj.food_id==food_id:
                        while(True):
                            message=str("Enter option to update"+
                                        '\n1 Name\n2 Quantity\n3 Price\n4 Discount\n5 Stock\n6 All\nany other to exit()\n')
                            try:
                                option=int(input(message))
                            except:
                                break
                            if option==1:
                                name=input("Enter new value: ")
                                food_obj.set_name(name)
                            elif option==2:
                                quantity=input("Enter new value: ")
                                food_obj.set_quantity(quantity)
                            elif option==3:
                                price=float(input("Enter new value: "))
                                food_obj.set_price (price)
                            elif option==4:
                                discount=float(input("Enter new value: "))
                                food_obj.set_discount (discount)
                            elif option==5:
                                stock=int(input("Enter new value: "))
                                food_obj.set_stock( stock)
                            elif option==6:
                                food_dict=self.get_details()
                                food_obj.update_all(**food_dict)
                            else:
                                break
                        not_found=False
                        print(f'{self.star*4} Successful {self.star*4}')
                        break
                if not_found:
                    print("Food item not found")    
            elif choice==4:
                not_found=True
                print(f'{self.star*10} Delete food item {self.star*10}')
                food_id=int(input("enter food id: "))
                for food_obj in self.food_list:
                    if food_obj.food_id==food_id:
                        self.food_list.remove(food_obj)
                        not_found=False
                        print(f'{self.star*4} Successful {self.star*4}')
                        break
                if not_found:
                    print("Food item not found")    
            elif choice==3:
                print(f'{self.star*10} All food items {self.star*10}')
                for food_obj in self.food_list:
                    print(f'Food_id:\t{food_obj.get_food_id()}',
                    f'Name    :\t{food_obj.get_name()}',
                    f'Quantity:\t{food_obj.get_quantity()}',
                    f'Price:   \t{food_obj.get_price()}',
                    f'Discount:\t{food_obj.get_discount()}',
                    f'Stock:   \t{food_obj.get_stock()}',sep='\n')
            elif choice==5:
                break

            else:
                print('invalid choice')