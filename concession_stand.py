# concession stand program
# practice the use of dictionaries 

menu = {"Pizza": 690,
        "Chessy Fries": 200,
        "Burger": 185,
        "Loaded Nachos": 275,
        "Tacos": 390,
        "Burrito": 255,
        "Fresh Lime Soda": 115}

cart = []
total = 0

print("-----------MENU-----------")
for a,b in menu.items():
    print(f"{a:17}: Rs {b}") 
print("--------------------------")

while True:
    food = input("Select an item (stop to exit): ").title()
    if food == "Stop":
        break 
    elif menu.get(food) is None:
        print(f"Sorry, we dont serve {food}")
    else: 
        cart.append(food)
        print(f"{food} added to cart")

print("--------YOUR CART--------")
for food in cart:
    total = total + menu.get(food)
    print(f"{food:^25}")

print(f"Your total is: Rs {total}")
print("-------------------------") 