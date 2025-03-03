import products
from stores import Store
from colorama import Fore

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]

def start():
    print("\n-----------------")
    print("Store Menu")
    print( "-----------------")
    print("")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

    users_choice = input("\nPlease enter your choice by number (1-4): ")
    return users_choice


def build_shopping_list():
    shopping_list = []

    while True:

        product_input = input("\nEnter the number for the product (or press Enter to finish): ")
        # Check if user wants to finish
        if product_input.strip() == "":
            print("Order quit!")
            print("\n-----------")
            break

        try:
            product_choice = int(product_input)
            # Check if the number is in the valid range
            if not (1 <= product_choice <= 3):
                raise ValueError("Number must be between 1 and 3")

            # Get quantity for the selected product
            while True:
                try:
                    quantity = int(input("What amount do you want? "))
                    break  # Exit the quantity loop if successful
                except ValueError:
                    print(Fore.RED + "No valid number entered! Enter only integers." + Fore.BLACK)
                    continue

            # Add the product and quantity as a tuple to the shopping list
            shopping_list.append((product_choice - 1 , quantity))
            print(f"Added product #{product_choice}, quantity: {quantity}")

        except ValueError as e:
            if "Number must be between" in str(e):
                print(Fore.RED + str(e) + Fore.BLACK)
            else:
                print(Fore.RED + "No valid number entered! Enter only integers." + Fore.BLACK)

    return shopping_list


def main():

    while True:
        user_choice = start()
        best_buy = Store(product_list)
        products = best_buy.get_all_products()

        if user_choice not in "1234":
            print(Fore.RED + "\nChoice not available! Type number for available commands!" + Fore.BLACK)
            continue

        if user_choice == "1":
            print(" ")
            for product in products:
                print(product.show())

        if user_choice == "2":
            print(" ")
            print(best_buy.get_total_quantity())

        if user_choice == "3":
            print("\nAvailable are: ")
            index = 1
            for product in products:
                products_info = product.show()
                print(f"{index}. {products_info}")
                index += 1

            shopping_list = build_shopping_list()
            new_shopping_list = []
            for product_nr, amount in shopping_list:
                new_shopping_list.append((products[product_nr], amount))
            best_buy.order(new_shopping_list)

        if user_choice == "4":
            print("Goodbye")
            break

if __name__ == "__main__":
    main()