class Product:
    def __init__(self, product_id, name, price, unit_cost, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.unit_cost = unit_cost
        self.stock = stock

    def get_product_id(self):
        return self.product_id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_unit_cost(self):
        return self.unit_cost

    def get_stock(self):
        return self.stock

    def calculate_profit(self):
        return self.price - self.unit_cost

    def display_product(self):
        print("\n----- PRODUCT DETAILS -----")
        print("Product ID:", self.product_id)
        print("Name      :", self.name)
        print("Price     :", self.price)
        print("Unit Cost :", self.unit_cost)
        print("Stock     :", self.stock)
        print("Profit    :", self.calculate_profit())


pid = int(input("Enter Product ID: "))
name = input("Enter Product Name: ")
price = float(input("Enter Price: "))
unit_cost = float(input("Enter Unit Cost: "))
stock = int(input("Enter Stock: "))

product1 = Product(pid, name, price, unit_cost, stock)

product1.display_product()
