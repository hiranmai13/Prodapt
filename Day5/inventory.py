warehouse=[]
n=int(input("Enter number of categories: "))
for i in range(n):
    category=input("\nEnter category name: ")
    products=[]
    m=int(input("Enter number of products: "))
    for j in range(m):
        product=input("Enter product name: ")
        quantity=int(input("Enter quantity: "))
        products.append([product, quantity])
    warehouse.append([category, products])

print("\nWarehouse Inventory")
for category in warehouse:
    print("\nCategory:", category[0])
    for product in category[1]:
        print("Product:", product[0], "Quantity:", product[1])