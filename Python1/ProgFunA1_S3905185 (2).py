#Creating list of names of custmers and custmer with membership.
Custmers = ["Rahul", "Naveen", "deepak", "Chander", "Mohan", "Aman", "Shalu", "kirti"]
Membership_Custmers = ["Rahul", "Chander", "Shalu", "Kirti"]
#Creating a dictionary that store the items available and the prices as their value.
products = {"Coca": 5, "Juice": 6, "Shirt": 10, "Towel": 12,
            "Oven": 20, "Beg": 25, "Mixer": 30}

flagg = True
flag=True
def menu():
    """Creating a function that print the menu on the screen.
        We don't need to pass any argument while calling menu() function."""
    print(20 * "_ _")
    print("    ")
    print("Welcome to RMIT retail management system")
    print(20 * "#")
    print("You have to choose from following options: ")
    print("1:  Place an order")
    print("2:  Add/update the products and price")
    print("3:  Dispaly existing Custumers")
    print("4:  Display existing custumers with membership")
    print("5:  Dispaly existing products")
    print("0:  Exit the program")
    print(20 * "#")


def placeOrder():
    """Function for accepting order of product from the custumers.
       And asks non-member custumers to apply for membership card.
       Also apply discount to the total amount if applicable."""
    Custmer_name = input("Enter your name: ")
    #checks if the custumer is in the list if not then add them to the list.
    if Custmer_name not in Custmers:
        Custmers.append(Custmer_name)
    #while loop runs until the custumer enters valid input.
    while flag :
        print("The Product in our Shop is this... \n")
        #displays the products available to order from.
        for key, val in products.items():
            print( key, "=>", val)
        product_name = input("Please enter the name of a valid product: ")
        Qantity_of_product = input("Enter the Quantity of the product: ")
        #checks if the input by the custumer is valid or not.
        if Qantity_of_product.isnumeric() and product_name in products and Qantity_of_product != (0):
            break
        else:
            print("Please enter the correct item and Quantity  ")
            continue
    #Asks the custumer to get the membership card to get the discount.
    flagg=True
    while flagg:
        if Custmer_name not in Membership_Custmers:
            membership_card = input("You want to apply for membershipcard press y or n: ")
            if membership_card ==  "y":
                Membership_Custmers.append(Custmer_name)
    #Checks if the custumer has membership card if true apply the discount.
        if Custmer_name in Membership_Custmers:
            print(Custmer_name, "purchases ", Qantity_of_product, "Pices of", product_name)
            print("Unit price :", products[product_name],"AUD")
            print(Custmer_name, "gets a discount of 5%")
            amount = int(products[product_name]) * int(Qantity_of_product)#calculating the total amount.
            print("Original Price is = ",amount )
            Discount = float((5 *amount/100 ))#calculating the discount on the total amount.
            print("Discount: ", Discount)
            print("Original Price : ",amount-Discount)
            break
        elif Custmer_name not in Membership_Custmers:
            if membership_card == "n":
        #if the custumer don't have the membership card we won't apply the discount.
                print(Custmer_name, "purchases ", Qantity_of_product, "Pices of ", product_name)
                print("Unit price : ",products[product_name], "AUD")
                print(Custmer_name, "You don't have Membership Card, so you are not Eligible For the Discount")
                amount = int(products[product_name]) * int(Qantity_of_product)
                print("Total price: ", float(amount))
                break
        else:
            print("Please enter from y and n")
            continue
            
        

def updateProducts():
    """This function will be called when we want to update the price of an existing product,
       or we want to add a new product in our store."""
    flag = True
    print("You Choose Add New product and update existing Product")
    # number of product you want to update and add
    while flag:
        print("Select from below options:")
        print("1. Add/Update products or price.\n2. Exit.")
        choice = input("Enter your choice: ")
        if choice == "1":
            product = input("Enter the name of the product: ")
            price = input("Enter the price of the product: ")
            #checks if the input by the custumer is correct or not.
            if product.isalpha() and price.isnumeric():
                products[product] = int(price)
            else:
                print(2*"\n")
                print("Enter a valid product name or price.")
                print(2*"\n")
        elif choice == "2":
            flag = False
#using while to continuously print the menu on the screen and take choice of custumer as input. And perform task according to that.
while True:
    menu()
    option = int(input("Enter the value from 1 to 5: "))
    #using if elif ladder for performing switch functionality.
    if option == 1:
        placeOrder()
    elif option == 2:
        updateProducts()
    elif option == 3:
        print(2*"\n")
        print("The existing Custmers list: ")
        #using for loop for display the custmers
        for c in Custmers:
            print(c)
        print(2*"\n")
    elif option == 4:
        print("The existing membership custmers list: ")
        print(2*"\n")
        for c in Membership_Custmers:
            print(c)
        print(2*"\n")
    elif option == 5:
        print("The existing product and their prices")
        print(2*"\n")
        #using for loop for display the existing products
        for key, val in products.items():
            print( key, "=>", val)
        print(2*"\n")
    elif option == 0:
        exit(0)
    else:
        print("Enter a valid option.")


