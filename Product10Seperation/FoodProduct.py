from product import Product

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


product2 = FruitProduct(102, "Apple" , 25 , 5 , "October 6, 2027"  , "Yes" , 90 )
product2.display_product()