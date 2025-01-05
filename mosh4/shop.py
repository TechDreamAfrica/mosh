class Product:
    # make constant
    DISCOUNT_PERCENTAGE = 0.50

    def __init__(self, title, price, qty):
        self.title = title
        self.price = price
        self.qty = qty

    def __str__(self):
        return self.title

    @classmethod
    def initial_values(cls):
        return cls("", 0.0, 0)

    def calc_total_price(self):
        total_price = self.price * self.qty
        return f"total price of {self.qty} quantities of {self.title} is ${total_price}"

    def apply_discount(self):
        discounted_price = self.price * self.DISCOUNT_PERCENTAGE
        self.price -= discounted_price
        return f"discounted price of {self.qty} quantities of {self.title} is ${discounted_price}"

product = Product.initial_values()

laptop = Product("HP Pro book Laptop", 2500, 3)
get_total_price = laptop.calc_total_price()
get_discounted_price = laptop.apply_discount()
print(get_total_price)
print(get_discounted_price)

phone = Product("Infinix Hot 40", 1300, 30)
get_total_price = phone.calc_total_price()
get_discounted_price = phone.apply_discount()
print(get_total_price)
print(get_discounted_price)