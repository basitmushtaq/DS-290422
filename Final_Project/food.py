class Food:

    def __init__(self,**kwargs):
        self.food_id=kwargs['id']
        self.name=kwargs['name']
        self.quantity=kwargs['quantity']
        self.price=kwargs['price']
        self.discount=kwargs['discount']
        self.stock=kwargs['stock']
    def get_food_id(self):
        return self.food_id
    


    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name

    def set_quantity(self,quantity):
        self.quantity=quantity
    def get_quantity(self):
        return self.quantity
    

    def set_price(self,price):
        self.price=price
    def get_price(self):
        return self.price

    
    def set_discount(self,discount):
        self.discount=discount
    def get_discount(self):
        return self.discount


    def set_stock(self,stock):
        self.stock=stock
    def get_stock(self):
        return self.stock

    def update_all(self,**kwargs):
        self.set_name(kwargs['name'])
        self.set_quantity(kwargs['quantity'])
        self.set_price (kwargs['price'])
        self.set_discount (kwargs['discount'])
        self.set_stock( kwargs['stock'])
    
    