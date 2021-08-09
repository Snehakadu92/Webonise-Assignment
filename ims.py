#Shop Inventory System


#Dictionaries
unit_price={}
description={}
company={}
stock={}

#Open file with stock
details = open("inventory.txt","r")

#First line of the file is the number of items
no_items  = int((details.readline()).rstrip("\n"))

#Add items to dictionaries
for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=float(x2)
    unit_price.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    description.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    company.update({x1: x2})

for i in range(0,no_items):
    line  = (details.readline()).rstrip("\n")
    x1,x2 = line.split("#")
    x1=int(x1)
    x2=int(x2)
    stock.update({x1: x2})

details.close()

#List to store the items purchased
cart=[]

c="y" #Runs the while loop as long as user wants


#Instructions
print("***** Welcome to shop Inventory *****")
print()
n = int(input("Enter whether you are shopkeeper or customer. \nIf you are shopkeeper please enter 1. \nfor Customer Please enter 2\n"))
if n == 1:
    total_cost=0 
    flag=0 #To check if they have checked out


    while(c!= "q" or c!= "Q"):
        print("1-Add an item")
        print("2-Remove an item")
        print("3-Edit specifics of an item")
        print("4-List all items")
        print("5-Inquire about all products")
        print("6-Purchase")
        print("7-Checkout")
        print("8-Show all products purchased")
        print("Q-Quit")
        print("remove-Remove an item from the cart")
        print()
        c= input("What would you like to do? ")
        
        if(c=="q" or c=="Q"):
            break
            
        elif(c=="1" or c=="1"):#Add a product
            p_id = int(input("Enter Item number: "))
            p_pr = float(input("Enter Item price: "))
            p_desc = input("Enter cart description: ")
            p_comp = input("Enter product company: ")
            p_stock = int(input("Enter Total stock: "))
            
            m=0
            for i in range(0,len(unit_price)):
                if(p_id in unit_price):
                    p_id+=1
                    m=1
            if(m==1):
                print()
                print("That product number already exists :(), changing value to ",p_id)
                    
            unit_price.update({p_id: p_pr})
            description.update({p_id: p_desc})
            company.update({p_id: p_comp})
            if(p_stock > -1):
                stock.update({p_id: p_stock})
            else:
                p_stock = 0
                stock.update({p_id: p_stock})
                print("The stock of an item cannot be negative, the stock has been set to 0.")
            print()
            print("product id: ",p_id,"\nDescription: ",description.get(p_id),"\nPrice: ",unit_price.get(p_id),"\nStock: ",stock.get(p_id))
            print("product was added successfully!")
            print()
            
        elif(c=="3"):#Edit a product
            print()
            p_id = int(input("Enter product id: "))
            if(p_id in unit_price):
                p_pr = float(input("Enter product price: "))
                p_desc = input("Enter product description: ")
                p_comp = input("Enter product company: ")
                p_stock = int(input("Enter product stock: "))
                    
                unit_price.update({p_id: p_pr})
                description.update({p_id: p_desc})
                company.update({p_id: p_comp})
                stock.update({p_id: p_stock})
                
            else:
                print("That item does not exist, to add an item use 1")
            print()
        
                
        elif(c=="2"):#Remove a product
            print()
            p_id = int(input("Enter product id: "))
            if(p_id in unit_price):
                are_you_sure = input("Are you sure you want to remove that item(y/n)? ")
                if(are_you_sure=="y" or are_you_sure=="Y"):
                    unit_price.pop(p_id)
                    description.pop(p_id)
                    stock.pop(p_id)
                    print("Item successfully removed!")
                print()
            else:
                print("Sorry, we don't have such an item!")
                print()
            
        elif(c=="4"):#List all the products
            print()
            print("products id and their prices: ",unit_price)
            print("products id and Descriptions: ",description)
            print("Company: ",company)
            print("Stock left of Item: ",stock)
            print()

        elif(c=="5"):#Inquire about all product
            print()
            p_id=int(input("Enter product Id: "))
            if(p_id in unit_price):
                print()
                print("product number: ",p_id,"\nDescription: ",description.get(p_id),"\nPrice: ",unit_price.get(p_id),"\nStock: ",stock.get(p_id))
                if(stock.get(p_id)<3 and stock.get(p_id)!=0):
                    print("Only ",stock.get(p_id)," remaining! Hurry!")
                print()
            else:
                print("Sorry we don't have such an item!")
                print()
            
        elif(c=="6"):#Purchase a product
            print()
            p_id = int(input("Enter product id: "))
            if(p_id in unit_price):
                if(flag==1):
                    flag=0
                stock_current = stock.get(p_id)
                if(stock_current>0):
                    stock_current = stock.get(p_id)
                    stock[p_id] = stock_current-1
                    item_price = unit_price.get(p_id)
                    total_cost = total_cost+item_price
                    print(description.get(p_id),"added to cart: ","$",item_price)
                    cart.append(p_id)#Stores item in cart
                else:
                    print("Sorry! We don't have that item in stock!")
            else:
                    print("Sorry! We don't have such an item!")
            print()
            
        elif(c=="7"):#Check out
            print()
            print("You bought the following products: ",cart)
            print("Total: ","$",round(total_cost,2))
            tax= round(0.13*total_cost,2)
            print("Tax is 13%: ","$",tax)
            total = round(total_cost+tax,2)
            print("After Tax: ","$",total)
            total_cost=0
            flag=1
            print()
            print("You can still purchase items after check out, your cart has been reset. To quit press q")
            print()
            
            
        elif(c=="remove" or c=="Remove"):#To remove an item from the cart
            print()
            are_you_sure = input("Are you sure you want to remove an item from the cart(y/n)? ")
            if(are_you_sure=="y"):
                p_id = int(input("Enter product id to remove from cart: "))
                if(p_id in cart):
                    stock_current = stock.get(p_id)
                    stock[p_id] = stock_current+1
                    item_price = unit_price.get(p_id)
                    total_cost = total_cost-item_price
                    j=0
                    for i in range(0,len(cart)):#To find the index of the product in the list cart
                        if(i==p_id):
                            j=i

                    cart.pop(j)
                    print(description.get(p_id),"removed from cart: ")
                    print()
                else:
                    print()
                    print("That item is not in your cart!")
                    print()
                    
        elif(c=="8"):#prints list of cart
            print()
            print(cart)
            print()
            
        else:
            print()
            print("ERROR!!")
            print()


    #Outputs total if the user quits without checking out
    if(total_cost>0 and flag==0):
        print()
        print("You bought: ",cart)
        print("Total: ","$",round(total_cost,2))
        tax= round(0.13*total_cost,2)
        print("Tax is 13%: ","$",tax)
        total = round(total_cost+tax,2)
        print("After Tax: ","$",total)
        
    print()
    print("Thank you for using Shop inventory")

    #Write the updated inventory to the file
    details = open("inventory.txt","w")
    no_items=len(unit_price)
    details.write(str(no_items)+"\n")
    for i in range(0,no_items):
        details.write(str(i+1)+"#"+str(unit_price[i+1])+"\n")
        
    for i in range(0,no_items):
        details.write(str(i+1)+"#"+description[i+1]+"\n")

    for i in range(0,no_items):
        details.write(str(i+1)+"#"+company[i+1]+"\n")
        
    for i in range(0,no_items):
        details.write(str(i+1)+"#"+str(stock[i+1])+"\n")
        
    details.close()
elif(n == 2):
    #Cutomer code
    print("Welcome to customer interface")
    total_cost = 0
    while(c!= "q" or c!= "Q"):
        print("1-List all Products")
        print("2-Search Product")
        print("3-Buy Products")
        c= input("What would you like to do? ")
        if(c=="1"):#List all the products
            print()
            print("products id and their prices: ",unit_price)
            print("products id and Descriptions: ",description)
            print("Company: ",company)
            print("Stock left of Item: ",stock)
            print()
        elif(c=="2"):#Inquire about all product
            print()
            p_id=int(input("Enter product Id: "))
            if(p_id in unit_price):
                print()
                print("product id: ",p_id,"\nCompany: ",company.get(p_id),"\nDescription: ",description.get(p_id),"\nPrice: ",unit_price.get(p_id),"\nStock: ",stock.get(p_id))
                if(stock.get(p_id)<3 and stock.get(p_id)!=0):
                    print("Only ",stock.get(p_id)," remaining! Hurry!")
                print()
            else:
                print("Sorry we don't have such an item!")
                print()
        elif(c=="3"):#Purchase a product
            print()
            p_id = int(input("Enter product id: "))
            if(p_id in unit_price):
                stock_current = stock.get(p_id)
                if(stock_current>0):
                    stock_current = stock.get(p_id)
                    stock[p_id] = stock_current-1
                    item_price = unit_price.get(p_id)
                    total_cost = total_cost+item_price
                    print(description.get(p_id),"added to cart: ","$",item_price)
                    cart.append(p_id)#Stores item in cart
                    Card_number = int(input("Please enter your card number: "))
                    CVV_No = int(input("please enter your cvv number: "))
                    #Write customer details in orders.txt file
                    f = open("Orders.txt", "w")
                    f.write("Products you have purchased: \n")
                    f.write("Card_number: \n")
                    f.write("CVV_No: \n")
                    f.close()
                                      
                else:
                    print("Sorry! We don't have that item in stock!")
            else:
                print("Sorry! We don't have such an item!")
            print()

else:
    print("Enter valid number")
