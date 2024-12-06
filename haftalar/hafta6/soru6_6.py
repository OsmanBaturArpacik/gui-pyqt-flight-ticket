from itertools import product
"""
--------------------------------
|          Product             |
--------------------------------
| + name: str                  |
| + price: float               |
| - __stock: int               |
--------------------------------
| + __init__(name, price, stock)|
| + check_stock(quantity): bool|
| + update_stock(quantity): bool|
| + get_stock(): int           |
--------------------------------


--------------------------------
|          Customer            |
--------------------------------
| + name: str                  |
| + email: str                 |
| - __orders: list[Order]      |
--------------------------------
| + __init__(name, email)      |
| + add_order(order: Order)    |
| + get_orders(): list[Order]  |
--------------------------------


--------------------------------
|          Order               |
--------------------------------
| + customer: Customer         |
| + product: Product           |
| + quantity: int              |
| + is_processed: bool         |
| + total_price: float         |
--------------------------------
| + __init__(customer, product, quantity) |
| - __calculate_total(): float|
| + process_order(): bool      |
--------------------------------


--------------------------------
|       display_order_history  |
--------------------------------
| + display_order_history(customer: Customer): None |
--------------------------------
"""

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = float(price)
        self.__stock = stock

    def check_stock(self, quantity):
        if self.__stock >= quantity:
            self.__stock += quantity
            return True
        else:
            return False

    def update_stock(self, quantity):
        if self.__stock <= quantity:
            self.__stock -= quantity
            return True
        else:
            return False

    def get_stock(self):
        return int(self.__stock)


class Customer:
    def __init__(self, name, mail):
        self.name = name
        self.mail = mail
        self.__orders = list()

    def add_order(self, order):
        self.__orders.append(order)

    def get_orders(self):
        return self.__orders


class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = int(quantity)
        self.is_processed = False
        self.total_price = self.__calculate_total()

    def __calculate_total(self):
        return float(self.quantity * self.product.price)

    def process_order(self):
        if self.product.check_stock(self.quantity):
            if self.product.update_stock(self.quantity):
                self.customer.add_order(self)
                self.is_processed = True

        return bool(self.is_processed)


