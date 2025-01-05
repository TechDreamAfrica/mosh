products = [
    ("Laptop", 1200.00, 5),
    ("Smartphone", 800.00, 10),
    ("Headphones", 150.00, 25),
]

class Items:
    def __init__(self, title, price, qty):
        self.title = title
        self.price = price
        self.qty = qty

    @classmethod
    def initial_values(cls):
        return cls("", 0.0, 0)

    def calculate_total_price(self):
        total_price = self.price * self.qty
        return total_price

all_item = Items([item[0] for item in products], [item[1] for item in products], [item[2] for item in products])
get_total_price = all_item.calculate_total_price()
print(get_total_price)