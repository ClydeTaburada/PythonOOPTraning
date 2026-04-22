class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display_product(self):
        print("\n----- PRODUCT -----")
        print("ID   :", self.product_id)
        print("Name :", self.name)
        print("Price:", self.price)
        print("Stock:", self.stock)


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, stock, warranty_years):
        super().__init__(product_id, name, price, stock)
        self.warranty_years = warranty_years

    def display_product(self):
        super().display_product()
        print("Warranty:", self.warranty_years, "years")


class FruitProduct(Product):
    def __init__ (self, product_id, name, price, stock, expiry_date, organic , calories):
        super().__init__(product_id, name, price, stock)
        self.expiry_date = expiry_date
        self.organic = organic
        self.calories = calories

    def display_product(self):
        super().display_product()
        print("Expiration date:", self.expiry_date)
        print("Organic:", self.organic)
        print("Contain calories:", self.calories)

    


product1 = ElectronicProduct(101, "Laptop", 45000, 10, 2)
product2 = FruitProduct(102, "Apple" , 25 , 5 , "October 6, 2027"  , "Yes" , 90 )
product1.display_product()
product2.display_product()