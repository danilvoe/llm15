class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def get_orders(self):
        return self.orders

    def update_email(self, new_email):
        self.email = new_email

    def __str__(self):
        return f"User: {self.name}, Email: {self.email}"


class Product:
    def __init__(self, name, price, stock=0):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, amount):
        self.stock += amount

    def is_available(self):
        return self.stock > 0

    def get_price(self):
        return self.price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}"


class Order:
    def __init__(self, user, products=None):
        self.user = user
        self.products = products or []
        self.total_price = 0

    def add_product(self, product):
        if product.is_available():
            self.products.append(product)
            self.total_price += product.get_price()

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            self.total_price -= product.get_price()

    def get_total(self):
        return self.total_price

    def confirm_order(self):
        for product in self.products:
            product.update_stock(-1)
        self.user.add_order(self)
        return f"Order confirmed. Total: {self.total_price}"

    def __str__(self):
        return f"Order by {self.user.name}, Total: {self.total_price}"


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def find_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def list_products(self):
        return [str(p) for p in self.products]

    def get_total_inventory_value(self):
        total = 0
        for product in self.products:
            total += product.get_price() * product.stock
        return total

    def __str__(self):
        return f"Store: {self.name}"


class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.items = []

    def add_item(self, product):
        if product.is_available():
            self.items.append(product)

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)

    def get_total(self):
        return sum(item.get_price() for item in self.items)

    def checkout(self):
        order = Order(self.user, self.items)
        return order.confirm_order()

    def __str__(self):
        return f"Shopping Cart for {self.user.name}, Items: {len(self.items)}"