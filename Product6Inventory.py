class Product:
    def __init__(self, product_id, name, price, unit_cost, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.unit_cost = unit_cost
        self.stock = stock

    def calculate_profit(self):
        return self.price - self.unit_cost

    def calculate_total_profit(self):
        return self.calculate_profit() * self.stock

    def display_product(self):
        print("\n==============================")
        print("      PRODUCT DETAILS")
        print("==============================")
        print("Product ID :", self.product_id)
        print("Name       :", self.name)
        print("Price      :", self.price)
        print("Unit Cost  :", self.unit_cost)
        print("Stock      :", self.stock)

        if self.price < self.unit_cost:
            print("Warning    : Loss-making product!")
        else:
            print("Profit     :", self.calculate_profit())

        print("Total Profit:", self.calculate_total_profit())
        print("==============================\n")


products = []
count = int(input("How many products do you want to add? "))
for i in range(count):
    print(f"\nEnter details for Product {i + 1}")

    pid = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    unit_cost = float(input("Enter Unit Cost: "))
    stock = int(input("Enter Stock: "))

    product = Product(pid, name, price, unit_cost, stock)
    products.append(product)

print("\n\n===== ALL PRODUCTS =====")
for p in products:
    p.display_product()

# Search product by ID
search_id = int(input("Enter Product ID to search: "))

found = False
for p in products:
    if p.product_id == search_id:
        print("\nProduct Found!")
        p.display_product()
        found = True
        break

if not found:
    print("Product not found.")