#Define the menu of restraunt
menu = {
    'Pasta':80,
    'Pizza':100,
    'ColdCoffe':120,
    'Sandwich':50,
    'Burger':50
}
 
#Greet the customer first
print("Welcome to our PYHTON cafe")
print("Pasta :Rs80\nPizza :Rs100\nColdCoffe :Rs120\nSandwich :Rs50\nBurger :Rs50")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"Your {item_1} has add into your order")
else:
    print(f"Sorry we don't have it in our menu , Please order something else we can serve you")
another_order = input("Do you want to order somehting else?(Yes/No)")
if another_order == "Yess":
        item_2 = input("Enter the name of the item= ")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Item {item_2} has been added to order")
        else:
            print(f"Ordered item {item_2} is not available, Please order something else")
else:
        print(f"Enjoy your fastfood")
print(f"The total amount of items to pay is {order_total}")      
