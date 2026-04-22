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