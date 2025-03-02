class Store:

    def __init__(self, products):
        self.products = products if products is not None else []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
       return sum(product.quantity for product in self.products)

    def get_all_products(self):
        return [product for product in self.products if product.active ]

    """active_products = []
        for product in products:
            if self.active:
                active_products.append(product)
            else:
                continue
        return active_products"""

    def order(self, shopping_list):
        """Process an order of products.
        Args:
        shopping_list: List of tuples (product, quantity) to order.
        Returns:
        float: Total price of the order.
        Raises: Exception: If a product doesn't have enough quantity in stock.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception(f"Product {product.name} not available!")
            if product.quantity < quantity:
                raise Exception(f"Not enough items in stock")

            product.quantity -= quantity
            total_price += float(product.price * quantity)
            print(f"{product.quantity} * {product.name} "
                  f"\n_____________________________________"
                  f"\nCost in total: {total_price} €")
            return total_price
