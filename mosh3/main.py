items = [
    ("Phone", 300),
    ("Laptop", 2341),
    ("Book", 4)
]

sorted_list = items.sort(key=lambda item:item[1])
print(items)

prices = [item[1] for item in items]
print(prices)

filtered = [item for item in items if item[1] >= 10]
print(filtered)