# Reflection:
# 1. Python lists are surprisingly flexible and dynamic, handling mixed types, easy slicing, and negative indexing effortlessly.
# 2. In inventory management, Python lists allow rapid sorting, filtering, and metric calculation (max/min/avg), saving time over manual Excel work.

# Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# Exercise 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as e:
    print("Tuples are immutable:", e)
print(coords)

# Exercise 6
sales = [100, 250, 75, 480, 200]
print("Total:", sum(sales))
print("Count:", len(sales))
print("Average:", sum(sales) / len(sales))
print("Best:", max(sales))
print("Worst:", min(sales))

# Exercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for p in prices:
    discounted.append(round(p * 0.9, 2))
print(prices)
print(discounted)

# Exercise 8
sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for s in sales_data:
    if s > 300:
        high_sales.append(s)
print(high_sales)
print(len(high_sales))
print(sum(high_sales) / len(high_sales))
