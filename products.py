from colorama import Fore, Style

class Product:
    """Represents a product in a store inventory system."""

    def __init__(self, name, price, quantity):
        """Initialize a Product with name, price, and quantity."""
        if not name:
            raise ValueError(Fore.RED + "Product name cannot be empty!" + Style.RESET_ALL)
        if price < 0:
            raise ValueError(Fore.RED + "Price cannot be negative!" + Style.RESET_ALL)
        if quantity < 0:
            raise ValueError(Fore.RED + "Quantity cannot be negative!" + Style.RESET_ALL)

        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            raise ValueError(Fore.RED + "Quantity must be a valid integer!" + Style.RESET_ALL)

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True


    def get_quantity(self):
        """Return the current quantity of the product."""
        return self.quantity


    def set_quantity(self, quantity):
        """Update the quantity and deactivate if it reaches zero."""
        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            raise ValueError(Fore.RED + "Quantity must be a valid integer!" + Style.RESET_ALL)

        if quantity < 0:
            raise ValueError(Fore.RED + "Quantity cannot be negative!" + Style.RESET_ALL)

        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()


    def is_active(self):
        """Check if the product is active and available for purchase."""
        return self.active


    def activate(self):
        """Make the product available for purchase."""
        self.active = True


    def deactivate(self):
        """Make the product unavailable for purchase."""
        self.active = False


    def show(self):
        """Return a formatted string with product details."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """Process a purchase and update inventory accordingly."""

        # First check if the product is active
        if not self.active:
            raise ValueError(Fore.RED + "Product is not active and cannot be purchased!" + Style.RESET_ALL)

        try:
            quantity = int(quantity)
        except (ValueError, TypeError):
            raise ValueError(Fore.RED + "Quantity must be a valid integer!" + Style.RESET_ALL)

        # Then check if the requested quantity is valid
        if quantity <= 0:
            raise ValueError(Fore.RED + "Quantity to buy must be at least 1!" + Style.RESET_ALL)

        # Finally check if we have enough stock
        if quantity > self.quantity:
            raise ValueError(Fore.RED + "Not enough items in stock!" + Style.RESET_ALL)

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)

        return total_price