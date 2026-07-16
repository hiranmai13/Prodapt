cart = []

def add_item(item):
    cart.append(item)
    print(f"{item} has been added to the cart.")

def remove_item(item):
    if item in cart:
        cart.remove(item)
        print(f"{item} has been removed from the cart.")
    else:
        print(f"{item} is not in the cart.")

def calculate_total(prices):
    return sum(prices)