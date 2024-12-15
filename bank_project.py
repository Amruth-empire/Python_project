# To create a Digital bank account
import sys
def show_balance(balance):
    print(f"Your account balance is ₹{balance:.2f}\n")

def deposit():
    amount=float(input("Enter an amount you want to deposit\n"))
    if amount <= 0:
        print("That is not a valid amount\n")
        return 0
    else:
        return amount 
    

def withdraw(balance):
    try:
        amount=float(input("Enter an amount you want to withdraw\n"))
        
        if amount > balance:
            print("Insuffient funds\n")
            return 0
        elif amount <= 0:
            print("Withdraw amount must be greater than zero\n")
            return 0
        else :
            return amount
    except ValueError:
        print("Invalid input! Please enter a numeric value.\n")
        return 0
        

def exit():
    print("Exiting the program. Have a great day!")
    sys.exit()


def main():
    balance=0
    while True:
        print(".....Banking program.....")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        try:
            choice=int(input("Enter your choice (1,4)\n"))
        
            # print(type(choice))
            if choice == 1:
                show_balance(balance)
            elif choice == 2:
                balance+=deposit()
            elif choice == 3:
                balance-= withdraw(balance)
            elif choice == 4:
                exit()
            else:
                print("Enter a valid choice\n")
        except ValueError: 
            print("Invalid input! Please enter a number between 1 and 4.\n")
            
print("Thank you for visiting the bank\n")
    

if __name__ == '__main__':
    main()