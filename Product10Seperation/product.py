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
