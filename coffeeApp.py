class Coffee:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order.")

    def total(self):
        return sum(item.price for item in self.items)

    def show_order(self):

        if not self.items:
            print("no items in order")
            return

        print("\n your order:")

        for i, item in enumerate(self.items, 1):
            print(f"Total: ${self.total()}\n")

    def checkout(self):

        if not self.items:
            print("your cart is empty.")
            return

        self.show_order()
        confirm = input("Proceed to checkout? (Yes/no): ").strip().lower()

        if confirm == "yes":
            print("Order confirmed! Thank you.")
            self.items.clear()

        else:
            print("checkout cancelled")

def main():
    menu = [

            Coffee("Espresso", 2.5),
            Coffee("Barista", 3.8),
            Coffee("Latte", 3.5),
            Coffee("Cappucino", 3.0)
    ]
    order = Order()
    while True:
        print("\n---- Coffee Menu ----")
        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price}")
        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")
        choice = input("Choose an option: ")
        if choice in ["1", "2", "3", "4"]:
            order.add_item(menu[int(choice) - 1])
        elif choice == "5":
            order.show_order()
        elif choice == "6":
            order.checkout()
        elif choice == "7":
            print("thank you for visiting!")
            break
        else:
            print("Invalid choice. Please Try Again.")

if __name__ == "__main__":
    main()
