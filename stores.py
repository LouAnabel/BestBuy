from products import Product
from colorama import Fore, Style


class Store:

    def __init__(self, products=None):
        # Default to empty list if products is None
        if products is None:
            self.products = []
        else:
            # Verify each item is a Product instance
            for product in products:
                if not isinstance(product, Product):
                    raise TypeError(Fore.RED + f"All items must be Product instances, got {type(product).__name__}" + Style.RESET_ALL)

            self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Returns the total quantity of all products as an integer."""
        sum_quantity = sum(product.quantity for product in self.products)
        quantity = int(sum_quantity)
        return quantity

    def get_all_products(self):
        return [product for product in self.products if product.active]

    def order(self, shopping_list):
        """Process an order based on a shopping list and return the total price."""
        total_price = 0
        order_details = []

        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(Fore.RED + f"Product is not available!" + Style.RESET_ALL)

            # Use product's buy method to ensure proper validation and deactivation logic
            item_price = product.buy(quantity)
            total_price += item_price
            order_details.append(Fore.BLUE + f"{quantity} * {product.name} for {product.price}€")

        # Print order summary
        for detail in order_details:
            print(detail)

        print(f"_____________________________________")
        print(f"Total price: {total_price:.2f} €" + Style.RESET_ALL)

        return total_price