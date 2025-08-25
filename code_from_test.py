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

    def reduce_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return True
        return False

    def add_stock(self, quantity):
        self.stock += quantity

    def get_price(self):
        return self.price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}"


class Order:
    def __init__(self, user, products=None):
        self.user = user
        self.products = products if products else []
        self.total = 0

    def add_product(self, product, quantity):
        if product.reduce_stock(quantity):
            self.products.append((product, quantity))
            self.total += product.get_price() * quantity
            return True
        return False

    def get_total(self):
        return self.total

    def finalize_order(self):
        self.user.add_order(self)
        return f"Order finalized. Total: {self.total}"

    def get_products(self):
        return self.products

    def __str__(self):
        return f"Order for {self.user.name}, Total: {self.total}"


class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.items = []

    def add_item(self, product, quantity):
        self.items.append((product, quantity))

    def get_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.get_price() * quantity
        return total

    def checkout(self):
        order = Order(self.user)
        for product, quantity in self.items:
            order.add_product(product, quantity)
        return order.finalize_order()

    def clear(self):
        self.items.clear()

    def get_items(self):
        return self.items


class Store:
    def __init__(self):
        self.products = []
        self.users = []

    def add_product(self, product):
        self.products.append(product)

    def register_user(self, user):
        self.users.append(user)

    def find_user(self, email):
        for user in self.users:
            if user.email == email:
                return user
        return None

    def get_products(self):
        return self.products

    def __str__(self):
        return f"Store with {len(self.products)} products and {len(self.users)} users"