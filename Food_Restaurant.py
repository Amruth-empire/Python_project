#Program to order a food items (Restaurant)
menu={
    "Samosa":20,
    "Popcorn":80,
    "Rice and Curry":120,
    "Pizza":60,
    "Burger":40
}

def main():
    total_fees=0
    print(".....Welcome to the Restaurant.....")
    for item, price in menu.items():
        print(f"{item} : Rs {price}")
    order_item1=input("Enter the food you want to order\n")
    if order_item1 in menu:
        total_fees+=menu[order_item1]
        print(f"Your item {order_item1} has been added your order")
    else:
        print(f"Your item {order_item1} is not available")
    another_order=input("Do you want to order another item (Yes/No)")
    if another_order.lower() == "yes":
    
        order_item2=input("Enter the name of the second food\n")
        if order_item2 in menu:
            total_fees+=menu[order_item2]
            print(f"Your item {order_item2} has been ordered")
        else:
            print(f"Your item {order_item2} is not available")
     
    print(f"The total amount of item is to pay {total_fees}")       
        
        
if __name__ == '__main__':
    main()
    

    