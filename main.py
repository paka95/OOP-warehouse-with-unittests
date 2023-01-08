from warehouse import Warehouse
from user import User

def main():
    new_warehouse = Warehouse(10,20,50)
    new_customer = User("Mike", 500)

    while True:
        print("======SPORT SHOP======")
        print(new_warehouse)
        print("""
        1. Buy shoes (€99.99)
        2. Buy pants (€76.95)
        3. Buy jackets (€129.99)
        4. Display customer information
        5. Upgrade your account
        6. Exit
        """)

        choice = int(input("Please specify your choice: "))

        if choice == 1:
            quantity = int(input("How many shoes would you like to buy?: "))
            bill = new_warehouse.buy_shoes(quantity, new_customer)
            new_customer.checkout(bill)
        elif choice == 2:
            quantity = int(input("How many pants would you like to buy?: "))
            bill = new_warehouse.buy_pants(quantity, new_customer)
            new_customer.checkout(bill)
        elif choice == 3:
            quantity = int(input("How many jackets would you like to buy?: "))
            bill = new_warehouse.buy_jacket(quantity, new_customer)
            new_customer.checkout(bill)
        elif choice == 4:
            print(new_customer)
        elif choice == 5:
            new_customer.upgrade_account()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Sorry, wrong option. Please choose 1-6")
            continue


if __name__ == '__main__':
    main()