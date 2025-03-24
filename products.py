class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Product name cannot be empty!")
        if price < 0:
            raise ValueError("Price cannot be negative!")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")

        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            raise ValueError("Quantity must be a valid integer!")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            raise ValueError("Quantity must be a valid integer!")

        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")

        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        # First check if the product is active
        if not self.active:
            raise ValueError("Product is not active and cannot be purchased!")

        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            raise ValueError("Quantity must be a valid integer!")

        # Then check if the requested quantity is valid
        if quantity <= 0:
            raise ValueError("Quantity to buy must be at least 1!")

        # Finally check if we have enough stock
        if quantity > self.quantity:
            raise ValueError("Not enough items in stock!")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)

        # Print item purchase information
        print(f"- {quantity} x {self.name}: ${total_price:.2f}")

        return total_price