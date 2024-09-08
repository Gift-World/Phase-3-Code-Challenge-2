

class Customer:
    def __init__(self,name):
        self.name = name
        self._orders = []
        
        
    @property
    
    #Gets the customer's name
    def name(self):
        return self._name  
    
    @name.setter
    def name(self,value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value
        else:    
            raise ValueError("Name must be a string between 1 and 15 characters")  
        
    def orders(self):
        
        #Returns a list of orders for customer
        return self._orders
    
   # Adding an order to the customer's list

    def add_order(self, order):
        from order import Order
        if not isinstance(order,Order):
            raise TypeError("Order must be an instance of the Order class")   
        self._orders.append(order) 
        
        
    def coffee(self):
        from coffee import Coffee
        
        #Returns a unique set of coffee objects related to customer's orders
        return {order.coffee for order in self._orders if isinstance(order.coffee,Coffee)} 
        
        #Creating new orders
    def create_order(self,coffee,price):
        from order import Order
        new_order = Order(self,coffee,price)
        return new_order     #Returns the new order     
        
