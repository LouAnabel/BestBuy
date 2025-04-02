import products
from stores import Store
from colorama import Fore, Style


def start():
    """printing the menu"""
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


def get_product_number(products):
    """Get and validate product number from user."""
    while True:
        product_input = input("\nEnter the number for the product (or press Enter to finish): ")
        # Check if user wants to finish
        if product_input.strip() == "":
            print("Order quit!")
            print("\n-----------")
            return None

        try:
            product_choice = int(product_input)
            # Check if the number is in the valid range
            if not (1 <= product_choice <= len(products)):
                print(Fore.RED + f"Error: Number must be between 1 and {len(products)}" + Style.RESET_ALL)
                continue

            product_index = product_choice - 1
            selected_product = products[product_index]

            return product_index, selected_product

        except ValueError:
            print(Fore.RED + "Error: Please enter a valid product number" + Style.RESET_ALL)
            continue


def get_requested_quantity(product):
    """Get and validate quantity from user for a specific product."""
    while True:
        try:
            quantity = int(input(f"What amount of {product.name} do you want? "))
            if quantity <= 0:
                print(Fore.RED + "Error: Quantity must be at least 1" + Style.RESET_ALL)
                continue

            if quantity > product.get_quantity():
                print(Fore.RED + f"Error: Not enough stock. Only {product.get_quantity()} available" + Style.RESET_ALL)
                continue

            return quantity

        except ValueError:
            print(Fore.RED + "No valid number entered! Enter only integers." + Style.RESET_ALL)
            continue


def build_shopping_list(products):
    """Build a shopping list by collecting product selections and quantities."""
    shopping_list = []

    while True:
        result = get_product_number(products)
        if result is None:  # User chose to quit
            break

        product_index, selected_product = result
        quantity = get_requested_quantity(selected_product)

        shopping_list.append((product_index, quantity))
        print(f"Added {quantity} x {selected_product.name} to your cart")

    return shopping_list


def process_order(products, shopping_list):
    if not shopping_list:
        print(Fore.RED + "No items in cart." + Style.RESET_ALL)
        return 0

    total_price = 0
    print("\nOrder Summary:")

    for product_index, quantity in shopping_list:
        product = products[product_index]
        try:
            item_price = product.buy(quantity)
            total_price += item_price
        except ValueError as e:
            print(Fore.RED + f"Could not process {product.name}: {str(e)}" + Style.RESET_ALL)
            continue  # Skip to the next item if there's an error

    print(f"\nTotal Order Price: ${total_price:.2f}")
    return total_price


def display_all_products(products):
    """Display all products in the store."""
    print(" ")
    for product in products:
        print(product.show())


def display_total_quantity(store):
    """Display the total quantity of all products in the store."""
    print(" ")
    print(store.get_total_quantity())


def handle_shopping(store, products):
    """Handle the shopping process including building list and processing order."""
    print("\nAvailable Products:")
    for i, product in enumerate(products, 1):
        if product.is_active():
            print(f"{i}. {product.show()}")

    # First build the shopping list (multiple items)
    shopping_list = build_shopping_list(products)

    # Then process the order once when complete
    if shopping_list:
        new_shopping_list = []
        for product_nr, amount in shopping_list:
            new_shopping_list.append((products[product_nr], amount))

        # Only call store.order() and remove process_order()
        try:
            store.order(new_shopping_list)
        except ValueError as e:
            print(Fore.RED + f"Error processing order: {str(e)}" + Style.RESET_ALL)


def main():

    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]

    best_buy = Store(product_list)

    while True:
        user_choice = start()
        available_products = best_buy.get_all_products()

        if user_choice not in ["1", "2", "3", "4"]:
            print(Fore.RED + "\nChoice not available! Type number for available commands!" + Style.RESET_ALL)
            continue

        elif user_choice == "1":
            display_all_products(available_products)

        elif user_choice == "2":
            display_total_quantity(best_buy)

        elif user_choice == "3":
            handle_shopping(best_buy, available_products)

        elif user_choice == "4":
            print("Goodbye")
            break

if __name__ == "__main__":
    main()

