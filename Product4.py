# User Input
class Product:
    def set_product_id(self, product_id):
        self.product_id = product_id

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_unit_cost(self, unit_cost):
        self.unit_cost = unit_cost

    def set_stock(self, stock):
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
        return self.get_price() - self.get_unit_cost()

    def display_product(self):
        print("\n----- PRODUCT DETAILS -----")
        print("Product ID:", self.get_product_id())
        print("Name      :", self.get_name())
        print("Price     :", self.get_price())
        print("Unit Cost :", self.get_unit_cost())
        print("Stock     :", self.get_stock())
        print("Profit    :", self.calculate_profit())


product1 = Product()

product1.set_product_id(int(input("Enter Product ID: ")))
product1.set_name(input("Enter Product Name: "))
product1.set_price(float(input("Enter Price: ")))
product1.set_unit_cost(float(input("Enter Unit Cost: ")))
product1.set_stock(int(input("Enter Stock: ")))

product1.display_product()