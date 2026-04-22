from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    @abstractmethod
    def display_product(self):
        pass

    @abstractmethod
    def calculate_profit(self):
        pass

    @abstractmethod
    def get_final_price(self):
        pass


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, stock, warranty_years):
        super().__init__(product_id, name, price, stock)
        self.warranty_years = warranty_years

    def display_product(self):
        print("\n----- ELECTRONIC PRODUCT -----")
        print("ID       :", self.product_id)
        print("Name     :", self.name)
        print("Price    :", self.price)
        print("Stock    :", self.stock)
        print("Warranty :", self.warranty_years, "years")

    def calculate_profit(self):
        return self.price * 0.20

    def get_final_price(self):
        return self.price

class ClothingProduct(Product):
    def __init__(self, product_id, name, price, stock, size, color, material):
        super().__init__(product_id, name, price, stock)
        self.size = size
        self.color = color
        self.material = material

    def display_product(self):
        print("\n----- CLOTHING PRODUCT -----")
        print("ID       :", self.product_id)
        print("Name     :", self.name)
        print("Price    :", self.price)
        print("Stock    :", self.stock)
        print("Size     :", self.size)
        print("Color    :", self.color)
        print("Material :", self.material)

    def calculate_profit(self):
        return self.price * 0.35

    def get_final_price(self):
        return self.price * 0.90


product1 = ElectronicProduct(101, "Laptop", 45000, 10, 2)
product2 = ClothingProduct(201, "T-Shirt", 500, 50, "L", "Black", "Cotton")

product1.display_product()
print("Profit:", product1.calculate_profit())
print("Final Price:", product1.get_final_price())

product2.display_product()
print("Profit:", product2.calculate_profit())
print("Final Price:", product2.get_final_price())