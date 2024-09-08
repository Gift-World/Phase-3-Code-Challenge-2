 # Coffee Shop (Code Challenge 2)


## Description :
 - This is a simple coffee shop application that allows for the management of customers, coffee types, and orders.
 - Customers can place orders for coffee, and the application keeps track of which customers have ordered which coffee, as well as the orders placed for each coffee.

 ## Features

 - Creates customers with names.
 - Manages customer orders.
 - Creates coffees with names.
 - Calculate the average price of a coffee
 
 ## Prerequisites
  - For easy usage, make sure you have the following:
   
   1. A reliable laptop or computer with at least 8GB RAM , core i5, 500GB HDD and stable internet access.
2. An Operating System preferably Linux or Windows 10+.
3. A text editor capable of running Python such as Visual Studio Code.
4. You have installed `Python 3.7 `or later.


## Installation

### Alternative One

To use this repo, follow these steps:

1. Open the terminal/CLI on your computer.
2. Clone this repository by running the following command:

        git@github.com:Gift-World/Phase-3-Code-Challenge-2.git

3. Change directory to the repo folder:

        cd Phase-3-Code-Challenge-2

4. Open it in your Text Editor by running the command:

        code  .




### Alternative Two

- On the top right corner of this page there is a button labelled Fork.

- Click on Fork to create a copy of the repository to your github account.

- Follow the process described in Alternative One above.


## Running the application

1. On Vs Code ternminal, run `pipenv install`

- This installs any required dependencies
2. Run the command `pipenv shell`

- This creates an active environment for the python programme.

### Usage
 #### Customer.py file
 On your terminal run,

        customer1 = Customer("Charles")
        customer2 = Customer("Gift")

        print(f"Customer 1: {customer1.name}")
        print(f"Customer 2: {customer2.name}")

        #Output : Customer 1: Charles
        #output : Customer 2: "Gift"


 #### Coffee.py file 

 On your terminal run the following command:

        coffee1 = Coffee("Espresso")
        coffee2 = Coffee("Latte")


        print(f"Coffee 1: {coffee1.name}")
        print(f"Coffee 2: {coffee2.name}")

        #output : Coffee 1 : Espresso
        #output : Coffee 2 : Latte









## Author
 - Charles Gift           




        
 