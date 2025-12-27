# shopping cart program 
# to practice the use of 

print("Welcome to the restaurant")

foods = []
prices = []
total = 0.0

while True: 
    food = input("Enter food item (enter 'stop' to exit): ")
    if food.lower() == 'stop':
        break
    else : 
        price = float(input(f"Enter price of {food}: Rs "))
        foods.append(food)
        prices.append(price)

print("------YOUR CART------")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Your total is: Rs {total}")

coupon = input(f"Do you have discount coupon (Y for yes, N for No): ")
if coupon.upper() == 'Y':
    discount = float(input("Enter discount (%) : "))
    total = total - (discount/100) * total

tip = float(input("Add tip (%): "))
total = total + (tip/100) * total

print(f"Your final payable amount is: Rs {total}")