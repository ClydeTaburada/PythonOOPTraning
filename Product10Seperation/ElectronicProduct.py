from product import Product

class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, stock, warranty_years):
        super().__init__(product_id, name, price, stock)
        self.warranty_years = warranty_years

    def display_product(self):
        super().display_product()
        print("Warranty:", self.warranty_years, "years")

product1 = ElectronicProduct(101, "Laptop", 45000, 10, 2)
product1.display_product()