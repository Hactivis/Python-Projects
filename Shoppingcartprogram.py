
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit):")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}:"))
        foods.append(food)
        prices.append(price)

print("_____ Your CART_____")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"Your total is: Rs{total}")


