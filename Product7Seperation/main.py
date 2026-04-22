from product import Product

products = []
count = int(input("How many products do you want to add? "))
for i in range(count):
    print(f"\nEnter details for Product {i + 1}")

    pid = int(input("Enter Product ID: "))
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    unit_cost = float(input("Enter Unit Cost: "))
    stock = int(input("Enter Stock: "))

    product = Product(pid, name, price, unit_cost, stock)
    products.append(product)

print("\n\n===== ALL PRODUCTS =====")
for p in products:
    p.display_product()

# Search product by ID
search_id = int(input("Enter Product ID to search: "))

found = False
for p in products:
    if p.product_id == search_id:
        print("\nProduct Found!")
        p.display_product()
        found = True
        break

if not found:
    print("Product not found.")