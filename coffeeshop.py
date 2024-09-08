
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
        
        
        if not isinstance(order, Order):
                raise Exception("Order must be an instance of the Order class")
        self._orders.append(order)
            
            
            #Returning a unique list of customers that have ordered the coffee specifically
    def customers(self):
        
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
        
coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte") 

print(f"Coffee 1: {coffee1.name}")
print(f"Coffee 2: {coffee2.name}")
      


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
       
        if not isinstance(order,Order):
            raise TypeError("Order must be an instance of the Order class")   
        self._orders.append(order) 
        
        
    def coffee(self):
        
        
        #Returns a unique set of coffee objects related to customer's orders
        return {order.coffee for order in self._orders if isinstance(order.coffee,Coffee)} 
        
        #Creating new orders
    def create_order(self,coffee,price):
       
        new_order = Order(self,coffee,price)
        return new_order     #Returns the new order     
    
    @classmethod
    def most_aficionado(cls,coffee):
       
        orders = [order for order in Order.all if order.coffee == coffee]
        if not orders:
            return None
        
        customer_spending = {}
        for order in orders:
            customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price

        # Find the customer with the maximum spending
        most_aficionado_customer = max(customer_spending, key=customer_spending.get)
        return most_aficionado_customer

            
        
customer1 = Customer("Alice")
customer2 = Customer("Bob")

    

class Order:
    all = [] #Holds all the orders
    def __init__(self, customer, coffee, price):
        #Initializes the order with a customer, coffee, and price
        
        self.customer = customer
        
        self.coffee = coffee
        
        self.price = price
        # Adds the order to the specific customer and coffee list with orders
        coffee.add_order(self)
        
        customer.add_order(self)
        
        Order.all.append(self)  # Adds the order to the global list of all orders
       #Gets the price
    @property
    def price(self):
        return self._price
    
    #Sets the price
    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Price must be a positive number")
        
        if  not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        
        self._price = value  #Stores the prices
    
    #Gets the customer
    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    
    def customer(self, value):
      
        # Setter for the customer with validation
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of the Customer class.")
        self._customer = value  # Set the customer
    
    
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, value):
      
        # Setter for the coffee with validation
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be an instance of the Coffee class.")
        self._coffee = value  # Set the coffee
    

        
        
        
          