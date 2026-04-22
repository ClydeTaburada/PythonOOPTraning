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

product1 = Product()

product1.set_product_id(101)
product1.set_name("Laptop")
product1.set_price(45000)
product1.set_stock(10)

print("Product ID:", product1.get_product_id())
print("Product Name:", product1.get_name())
print("Product Price:", product1.get_price())
print("Product Stock:", product1.get_stock())
