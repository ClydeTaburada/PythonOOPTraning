class Product:
    def set_product_id(self, product_id):
        self.product_id = product_id

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_stock(self, stock):
        self.stock = stock

    def get_product_id(self):
        return self.product_id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock
    
    def display_product(self):
        print("\n----- PRODUCT DETAILS -----")
        print("Product ID:", self.get_product_id())
        print("Name      :", self.get_name())
        print("Price     :", self.get_price())
        print("Stock     :", self.get_stock())

product1 = Product()

product1.set_product_id(101)
product1.set_name("Laptop")
product1.set_price(45000)
product1.set_stock(10)

product1.display_product()