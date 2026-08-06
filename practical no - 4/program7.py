inventory = {}

def add():
    name = input("Enter product name: ")
    qty = int(input("Enter quantity: "))
    inventory[name] = qty

def update():
    name = input("Enter product name: ")
    if name in inventory:
        qty = int(input("Enter new quantity: "))
        inventory[name] = qty

        if qty == 0:
            del inventory[name]
            print("Product removed")
    else:
        print("Product not found")

def highest():
    max_product = max(inventory, key=inventory.get)
    print("Highest Stock Product:", max_product)
    print("Quantity:", inventory[max_product])

def total():
    print("Total Unique Products:", len(inventory))


def display():
    print(inventory)

add()
add()

display()

update()

display()

highest()

total()