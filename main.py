import products
from stores import Store
# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)

def start():
    print(f"Store Menu")
    print(f"-----------------")
    print(f"1. List all products in store")
    print(f"2. Show total amount in store")
    print(f"3. Make an order")
    print(f"4. Quit")

def main():
    start()

products = best_buy.get_all_products()
print(best_buy.get_total_quantity())
best_buy.order([(products[0], 1), (products[1], 2)])

if __name__ == "__main__":
    main()