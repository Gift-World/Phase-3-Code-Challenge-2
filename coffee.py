
class Coffee:
    def __init__(self, name):
        self._name=None
        #Initializes coffee with a name and an empty 
        self.name = name
       
        self._orders = []
            
          
       #Gets the coffee's name      
    @property
    def name(self):
        return self._name
    
    #Sets the coffee's name
    @name.setter
    def name(self, value):
        if hasattr(self, "_name") and self._name is not None:
            raise Exception("Cannot change the coffee's name")
        
        if not isinstance(value,str):
            raise Exception("Name must be a string")
        
        if len(value) < 3 :
            raise Exception("Name must be atleast 3 characters")
        
        self._name = value  #Sets the name if all the conditions are met
        
    #Returns the list of orders for the coffee
    def orders(self):
            return self._orders
        
        # Adding an order to the cofee list
    def add_order  (self, order):
        from order import Order
        
        if not isinstance(order, Order):
                raise Exception("Order must be an instance of the Order class")
        self._orders.append(order)
            
            
            #Returning a unique list of customers that have ordered the coffee specifically
    def customers(self):
        from customer import Customer
        customers_orders = set()
            
        for order in self._orders:
                if isinstance (order.customer,Customer):
                    customers_orders.add(order.customer)
        return list(customers_orders)   
        
        #Returning the total number of orders for the coffee
    def num_orders(self)  :
            return len(self._orders)  
        # Returning the average price of the coffee in relation to its orders
    def average_price(self):
            if not self._orders:
                return 0 #Returns 0 if there are no orders
            total_price = sum(order.price for order in self._orders) # sums all the order prices
            number_of_orders = len(self._orders) # counts the number of orders
            
            return total_price / number_of_orders    #Calculates the average price
        
        
        
 ##Example usage
 
 
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")        

print(f"Coffee 1: {coffee1.name}")
print(f"Coffee 2: {coffee2.name}")
      
 