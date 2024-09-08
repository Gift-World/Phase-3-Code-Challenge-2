
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
        from customer import Customer
        # Setter for the customer with validation
        if not isinstance(value, Customer):
            raise ValueError("Customer must be an instance of the Customer class.")
        self._customer = value  # Set the customer
    
    
    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        # Setter for the coffee with validation
        if not isinstance(value, Coffee):
            raise ValueError("Coffee must be an instance of the Coffee class.")
        self._coffee = value  # Set the coffee
    

