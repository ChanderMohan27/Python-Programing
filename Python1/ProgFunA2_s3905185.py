from datetime import datetime

# define customer class
class Customer:
    # constructor for Customer class
    def __init__(self, ID, Name, Value=0.0):
        self.ID = ID
        self.Name = Name
        self.Value = Value

    # getter for attribute
    def get_id(self):
        return self.ID
    
    def get_value(self):
        return self.Value
    
    
    def set_name(self,Name):
        self.Name = Name
    
    def set_value(self,Value):
        self.Value = Value
    def get_name(self):
        return self.Name
    #getter discount rate and price
    def get_discount(self,Price):
        return 0, Price 

    # display info function
    def display_info(self):
        print("Customer ID: ", self.ID)
        print("Customer Name: ", self.Name)
        print("Money spend Total: ", self.Value)
        Discount, Price = self.get_discount(self.Value) 
        print("Discount Rate: ", Discount * 100, "%")


#class Member
class Member(Customer):
 #constructer parameter from base class
    def __init__(self, Id, Name, Value=0, Discount__Rate=0.05):
        # parent class (Customer)
        super().__init__(Id, Name, Value)
        self.Discount_Rate = Discount__Rate
   
 #setter to set Rate    
    def set_rate(self,Discount__Rate):
        self.Discount_Rate = Discount__Rate

    #Get discount from price 
    def get_discount(self, Price):
        Discount = self.Discount_Rate * Price
        return self.Discount_Rate, (Price-Discount)

    #To display the customer_info 
    def display_info(self):
        Customer.display_info(self)


# class for VIP member 
class VIPMember(Customer):
    First_Discount_Rate=0.10 
    Second_Discount_Rate=0.15
    #Take arrguments from vip member class  
    def __init__(self, Id, Name, Value=0, First_Discount_Rate=0.10, Second_Discount_Rate=0.15):
        super().__init__(Id, Name, Value)
        self.First_Discount_Rate = First_Discount_Rate
        Second_Discount_Rate = (First_Discount_Rate*100+5)/100
        self.Second_Discount_Rate = Second_Discount_Rate
        self.threshold = 1000
    #set First_discount_rate and second_discount_rate    
    def set_rate(self, First_Rate):
        self.First_Discount_Rate = First_Rate
        self.Second_Discount_Rate = (self.First_Discount_Rate*100+5)/100

    # setter for threshold 
    def set_threshold(self, threshold=1000):
        self.threshold = threshold 
 
   #For discount from price  
    def get_discount(self, Price):  
        if Price<=self.threshold:
            discount = self.First_Discount_Rate * Price
            return self.First_Discount_Rate,(Price-discount) 
        else: 
            discount = self.Second_Discount_Rate * Price
            return self.Second_Discount_Rate,(Price-discount)        
        
    
    #display_info about VIP member
    def display_info(self):
        Customer.display_info(self)
        print('First_discount_Rate: ', self.First_Discount_Rate, '%')
        print('threshold_limit: ', self.threshold, '(AUD)')


# class for Products
class Product:
    Price=0.0 
    Stock=0   
    #  constructor which  takes the  arguments of  class
    def __init__(self, Product_Id, Product_Name, Price, Stock):
        self.Product_Id = Product_Id
        self.Product_Name = Product_Name
        self.Price = Price
        self.Stock = Stock

    # set method  for product_Id
    def set_id(self, Product_Id):
        self.Product_Id = Product_Id

    # getter method for product_ID
    def get_id(self):
        return self.Product_Id

    # setter for Product_Name
    def set_name(self, Product_Name):
        self.Product_Name = Product_Name

    # getter for Product Name
    def get_name(self):
        return self.Product_Name

    # setter for Product Price
    def set_price(self, Product_Price):
        self.Price = Product_Price

    # getter for Product Price
    def get_price(self):
        return self.Price

        # setter for Stock
    def set_Stock(self, Stock):
        self.Stock = Stock

        # getter for Stock
    def get_Stock(self):
        return self.Stock


# Order class
class Order:
    #constructor
    def __init__(self, Customer, Product, Quantity=0):
        self.Customer = Customer
        self.quantity = Quantity
        self.Product = Product
       #For date and time 
        now = datetime.now()
        self.Date = now.strftime("%d/%m/%Y %H:%M:%S")

    # setter and getter for Product function
    def set_Product(self, Prodct):
        self.Product = Prodct

    
    def get_Product(self):
        return self.Product

    
    def set_Customer(self, Customer):
        self.Customer = Customer

    
    def get_Customer(self):
        return self.Customer

    
    def set_quantity(self, Quantity):
        self.Quantity = Quantity

    
    def get_quantity(self):
        return self.Quantity

    
    def set_Date(self,Date):
        self.Date = Date
    
   
    def get_Date(self):
        return self.Date
    
    #display order
    def display_order(self):
        print('{}, {}, {}, {}'.format(self.Customer,self.Product,self.Quantity,self.Date))


# class Records
class Records(): 
    #using function for using the method of base class
    def __init__(self):
        self.Cust_list = []  
        self.Prod_list = []

    #read_all the customer from customer file
    def read_Customers(self):
        try:
            with open("customers.txt", "r") as files:
                for line in files:
                    Id,Name,discountt_rate,Value = line.split(",")
                    if Id[0]=='C':
                        Customerss = Customer(Id, Name,float(Value))
                    elif Id[0]=='M': 
                        Customerss = Member(Id, Name,float(Value),float(discountt_rate))
                    else:
                        Customerss = VIPMember(Id, Name,float(Value),float(discountt_rate))
                        
                    self.Cust_list.append(Customerss)    
                
        except:
            print("customer.txt file is not exist in this folder")
            exit(0) 
    
    
    # Find Customer using Find_Customer name or Id
    def Find_Customer(self, key):
        for Customer in self.Cust_list: 
            if Customer.get_id() == key or Customer.get_name() == key:
                return Customer
        
        return None
    #display all the customer from customer.txt
    def All_Customers(self):
        print('(ID,', 'Name,', 'Discount_Rate,', 'Value)')
        for Cust in self.Cust_list:
            disc = Cust.get_discount(Cust.get_value())
            print(Cust.get_id(), Cust.get_name(),disc[0]*100, '%', Cust.get_value())
            
    #read all the product from the product 
    def read_Products(self):
        try:
            with open("products.txt", "r") as file:
                for line in file:
                    Id,Name,Price,Stock = line.split(",")          
                    productss = Product(Id,Name,float(Price),int(Stock))
                    self.Prod_list.append(productss)
        except:
            print("Product.txt file is not exist in the system")
            exit(0)
    
    

    # Find Product Using the Find_product
    def Find_Product(self, key):
        
        for Product in self.Prod_list:
           
            if Product.get_id() == key or Product.get_name() == key:
                return Product
        
        return None
    
    # Display the product From product.txt
    def All_Products(self):
        print('(ID,', 'Name,', 'Price,', 'Stock)')
        for prod in self.Prod_list:
            print(prod.get_id(),prod.get_name(),prod.get_price(),prod.get_Stock())
                   
#Main Function

#Make a variable for Record class
rec = Records()
#read Customers for record
rec.read_Customers()
#read Products from record
rec.read_Products()

Custmer_ID = 9
Membr_ID = 12
ViPID = 11


# menu to take the  user input
while True:
    #print main menu
    print('Welcome to RMIT Retail Management System.\n')
    print('#################################################')
    print('Please choose from the following options:')
    print('press 1: Place an Order : ')
    print('press 2: Display existing Customers: ')
    print('press 3: Display existing Products:')
    print('press 4: Adjust the discount rates of a VIP member')
    print('press 5: Adjust the threshold limit of all VIP members')
    print('press 6: Display all orders')
    print('press 7: Display all orders of a Customer')
    print('press 8: Exit the program')
    print('#' * 20)
    
    #Take User_Input from user
    User_Input = input('Choose one option: ')
    
    #place an order when User_Input = 1 
    if User_Input == "1":
        
        #Take input the name of customer
        Name = input('Enter the Customer Name [e.g. Chander]:\n')
        #for valid product 
        while True:
            Product_Name = input('\nEnter the Product Name [enter a valid Product only e.g. TV, juicer, bag, heater]: \n')
            #Find Product from record
            Product  = rec.Find_Product(Product_Name)
            if Product !=None:
                break
            print('Please enter a valid Product!. The current product is not exist \n')
        
        #Take input product Quantity whenever user not put a valid input
        qnty = input('\nEnter the valid Product Quantity [enter a positive integer only ]:\n')   
        while not (qnty.isdigit() and Product.get_Stock()>=int(qnty) and int(qnty)>0):
            print('Product Quantity is not valid ')
            qnty = input('Enter the valid Product Quantity [enter a positive integer]:\n')   
        
        qnty = int(qnty)
        
        #Find Customer in the records
        customeer = rec.Find_Customer(Name)
        
        #UpDate Stock
        Product.set_Stock(Product.get_Stock()-qnty)
        
        #if customer is new than ask for membership 
        if customeer == None:
            #For user want a membership or not!!!
            Membership = input('\n You are our new Customer. Would you like to have our membership ?[y or n]:\n')
            while Membership!='n' and Membership!='y':
                Membership = input('\n This is a new Customer. Does the Customer want a membership[y or n]:\n')
            
            #For asking membership from a new customer
            if Membership == 'y':
                Membership_Type = input('\nWhat type of membership do you want enter M or V : \n ')
                while Membership_Type!='M' and Membership_Type!='V':
                    Membership_Type = input('\nWhat type of membership do you want enter M or V : \n')
                
                #When membership is member then customer is  Member object
                if Membership_Type=='M':
                    customeer = Member('M'+str(Membr_ID), Name)
                    Membr_ID+=1
                #When membership is a VIP member then VIP Member object as a Customer
                else:
                    customeer = VIPMember('V'+str(ViPID), Name,200)
                    ViPID+=1
            #If Not an membership than store as a simple customer 
            else:
                customeer = Customer('C'+str(Custmer_ID), Name)
                Custmer_ID+=1
            #Append a new customer in the records
            rec.Cust_list.append(customeer)
        else:
            customeer.set_name(Name)
        
        #getting data of a customer 
        Discut_Rate,Discut_price = customeer.get_discount(qnty * Product.get_price()) 
        customeer.set_value(customeer.get_value()+Discut_price)
       
        #print details of order of a customer
        print('\n**********#######***********\n\n\n\n')
        print(Name, 'purchase', qnty, 'x', Product_Name)
        print('unit Price              ', Product.get_price(), '(AUD)')
        print(Name, 'gets discount  of', Discut_Rate*100, '%.')
        print('Total Price:            ', Discut_price, '(AUD)')
        print('\n**********#######***********\n\n\n\n')
    #display all the Customers
    elif User_Input == "2":
        rec.All_Customers()
    #display all the Products
    elif User_Input == "3":
        rec.All_Products()
    
    #User_input = 4 is for set the discount rate
    elif User_Input == "4":
        #customer find on the bases of ID and Name
        key = input('Enter the name or ID of VIP member : ')
        Cust = rec.Find_Customer(key)
        #User Not found so print Invalid 
        if Cust==None:
            print('Customer is not valid!')
        #otherwise set the discount Rate of vip member
        else:
            Rate = float(input('Enter the first discount Rate of VIP member: '))
            Cust.set_rate(Rate)            
    
    #if User_Input is 5 then set the thresold limit
    elif User_Input == "5":
        threshold = int(input('Enter the thresold limit of all VIP members: '))
        #Set thresold limit  for VIP members
        for Cust in rec.Cust_list:
            if Cust.get_id()[0]=='V':
                Cust.set_threshold(threshold)
    
    elif User_Input == "0":
        print("exit")
        break
    #For correct input
    else:
        print('Enter correct input')
