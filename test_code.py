import unittest
from code_from_test import User, Product, Order, Store, ShoppingCart

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Alice", "alice@example.com")
        self.product = Product("Laptop", 1000, 5)

    def test_user_initialization(self):
        self.assertEqual(self.user.name, "Alice")
        self.assertEqual(self.user.email, "alice@example.com")
        self.assertEqual(len(self.user.orders), 0)

    def test_add_order(self):
        order = Order(self.user)
        self.user.add_order(order)
        self.assertIn(order, self.user.orders)

    def test_get_orders(self):
        order1 = Order(self.user)
        order2 = Order(self.user)
        self.user.add_order(order1)
        self.user.add_order(order2)
        orders = self.user.get_orders()
        self.assertEqual(len(orders), 2)

    def test_update_email(self):
        self.user.update_email("newemail@example.com")
        self.assertEqual(self.user.email, "newemail@example.com")

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product("Phone", 500, 10)

    def test_product_initialization(self):
        self.assertEqual(self.product.name, "Phone")
        self.assertEqual(self.product.price, 500)
        self.assertEqual(self.product.stock, 10)

    def test_update_stock(self):
        self.product.update_stock(5)
        self.assertEqual(self.product.stock, 15)

    def test_is_available(self):
        self.assertTrue(self.product.is_available())
        self.product.update_stock(-10)
        self.assertFalse(self.product.is_available())

    def test_get_price(self):
        self.assertEqual(self.product.get_price(), 500)

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.user = User("Bob", "bob@example.com")
        self.product1 = Product("Book", 20, 5)
        self.product2 = Product("Pen", 5, 10)
        self.order = Order(self.user)

    def test_order_initialization(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(len(self.order.products), 0)
        self.assertEqual(self.order.total_price, 0)

    def test_add_product(self):
        self.order.add_product(self.product1)
        self.assertIn(self.product1, self.order.products)
        self.assertEqual(self.order.get_total(), 20)

    def test_remove_product(self):
        self.order.add_product(self.product1)
        self.order.add_product(self.product2)
        self.order.remove_product(self.product1)
        self.assertNotIn(self.product1, self.order.products)
        self.assertEqual(self.order.get_total(), 5)

    def test_confirm_order(self):
        self.order.add_product(self.product1)
        result = self.order.confirm_order()
        self.assertIn("Order confirmed", result)
        self.assertIn("Total: 20", result)

class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = Store("Tech Store")
        self.product1 = Product("Laptop", 1000, 5)
        self.product2 = Product("Mouse", 25, 10)

    def test_store_initialization(self):
        self.assertEqual(self.store.name, "Tech Store")
        self.assertEqual(len(self.store.products), 0)

    def test_add_product(self):
        self.store.add_product(self.product1)
        self.assertIn(self.product1, self.store.products)

    def test_find_product(self):
        self.store.add_product(self.product1)
        found = self.store.find_product("Laptop")
        self.assertEqual(found, self.product1)

    def test_list_products(self):
        self.store.add_product(self.product1)
        self.store.add_product(self.product2)
        products = self.store.list_products()
        self.assertEqual(len(products), 2)

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.user = User("Charlie", "charlie@example.com")
        self.cart = ShoppingCart(self.user)
        self.product1 = Product("Book", 20, 5)
        self.product2 = Product("Pen", 5, 10)

    def test_cart_initialization(self):
        self.assertEqual(self.cart.user, self.user)
        self.assertEqual(len(self.cart.items), 0)

    def test_add_item(self):
        self.cart.add_item(self.product1)
        self.assertIn(self.product1, self.cart.items)

    def test_remove_item(self):
        self.cart.add_item(self.product1)
        self.cart.remove_item(self.product1)
        self.assertNotIn(self.product1, self.cart.items)

    def test_get_total(self):
        self.cart.add_item(self.product1)
        self.cart.add_item(self.product2)
        self.assertEqual(self.cart.get_total(), 25)

if __name__ == '__main__':
    unittest.main()