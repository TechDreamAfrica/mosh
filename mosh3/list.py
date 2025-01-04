products = [
    ("Apples (1kg)", 3.50),
    ("Bananas (1kg)", 2.80),
    ("Oranges (1kg)", 4.00),
    ("Milk (1L)", 1.50),
    ("Bread (1 loaf)", 2.00),
    ("Eggs (dozen)", 3.20),
    ("Chicken (1kg)", 6.50),
    ("Rice (5kg bag)", 12.00),
    ("Cooking Oil (1L)", 5.50),
    ("Pasta (500g)", 2.30),
    ("Sugar (1kg)", 1.80),
    ("Salt (1kg)", 0.90),
    ("Butter (250g)", 2.50),
    ("Cheese (200g)", 3.70),
    ("Yogurt (500ml)", 2.20),
    ("Chocolate Bar", 1.20),
    ("Coffee (200g)", 4.80),
    ("Tea (100 bags)", 3.40),
    ("Shampoo (250ml)", 4.00),
    ("Toothpaste (100ml)", 2.50),
    ("Soap (bar)", 1.50),
    ("Laundry Detergent (1kg)", 6.80),
    ("Dishwashing Liquid (500ml)", 2.90),
    ("Notebook", 1.00),
    ("Pen (pack of 5)", 2.00),
    ("Pencil (pack of 5)", 1.50),
    ("Eraser", 0.50),
    ("Water Bottle (1.5L)", 1.00),
    ("Juice (1L)", 3.00),
    ("Cereal (500g)", 4.50),
    ("Ice Cream (1L)", 5.00)
]

def sort_products():
    sorted_products = [product for product in products]
    return sorted_products

def filter_product_by_price():
    filtered = [product for product in products if product[1] >= 3]
    return filtered

def get_product_name():
    product_names = [product[0] for product in products]
    return product_names


print(sort_products())
print(filter_product_by_price())
print(get_product_name())