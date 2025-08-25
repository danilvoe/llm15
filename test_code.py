import unittest
from unittest.mock import Mock

# Импорт классов из модуля code_from_test
import code_from_test

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = code_from_test.User("John Doe", "john@example.com")
        self.product = code_from_test.Product("Test Product", 100, 10)
        
    def test_user_initialization(self):
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(len(self.user.orders), 0)
        
    def test_add_order(self):
        order = code_from_test.Order(self.user)
        self.user.add_order(order)
        self.assertIn(order, self.user.orders)
        
    def test_get_orders(self):
        order1 = code_from_test.Order(self.user)
        order2 = code_from_test.Order(self.user)
        self.user.add_order(order1)
        self.user.add_order(order2)
        orders = self.user.get_orders()
        self.assertEqual(len(orders), 2)
        
    def test_update_email(self):
        self.user.update_email("newemail@example.com")
        self.assertEqual(self.user.email, "newemail@example.com")

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = code_from_test.Product("Test Product", 100, 10)
        
    def test_product_initialization(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.price, 100)
        self.assertEqual(self.product.stock, 10)
        
    def test_reduce_stock_success(self):
        result = self.product.reduce_stock(5)
        self.assertTrue(result)
        self.assertEqual(self.product.stock, 5)
        
    def test_reduce_stock_failure(self):
        result = self.product.reduce_stock(15)
        self.assertFalse(result)
        self.assertEqual(self.product.stock, 10)
        
    def test_add_stock(self):
        self.product.add_stock(5)
        self.assertEqual(self.product.stock, 15)
        
    def test_get_price(self):
        self.assertEqual(self.product.get_price(), 100)

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.user = code_from_test.User("John Doe", "john@example.com")
        self.product1 = code_from_test.Product("Product 1", 100, 10)
        self.product2 = code_from_test.Product("Product 2", 50, 5)
        self.order = code_from_test.Order(self.user)
        
    def test_order_initialization(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(len(self.order.products), 0)
        self.assertEqual(self.order.total, 0)
        
    def test_add_product_success(self):
        result = self.order.add_product(self.product1, 2)
        self.assertTrue(result)
        self.assertEqual(len(self.order.products), 1)
        self.assertEqual(self.order.total, 200)
        
    def test_add_product_failure(self):
        result = self.order.add_product(self.product1, 15)
        self.assertFalse(result)
        self.assertEqual(len(self.order.products), 0)
        
    def test_get_total(self):
        self.order.add_product(self.product1, 2)
        self.order.add_product(self.product2, 1)
        self.assertEqual(self.order.get_total(), 250)
        
    def test_finalize_order(self):
        self.order.add_product(self.product1, 2)
        result = self.order.finalize_order()
        self.assertIn("Order finalized", result)
        self.assertIn("Total: 200", result)
        self.assertIn(self.order, self.user.orders)

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.user = code_from_test.User("John Doe", "john@example.com")
        self.product1 = code_from_test.Product("Product 1", 100, 10)
        self.product2 = code_from_test.Product("Product 2", 50, 5)
        self.cart = code_from_test.ShoppingCart(self.user)
        
    def test_cart_initialization(self):
        self.assertEqual(self.cart.user, self.user)
        self.assertEqual(len(self.cart.items), 0)
        
    def test_add_item(self):
        self.cart.add_item(self.product1, 2)
        self.assertEqual(len(self.cart.items), 1)
        
    def test_get_total(self):
        self.cart.add_item(self.product1, 2)
        self.cart.add_item(self.product2, 1)
        self.assertEqual(self.cart.get_total(), 250)
        
    def test_checkout_success(self):
        self.cart.add_item(self.product1, 2)
        result = self.cart.checkout()
        self.assertIn("Order finalized", result)
        self.assertIn("Total: 200", result)
        
    def test_clear(self):
        self.cart.add_item(self.product1, 2)
        self.cart.clear()
        self.assertEqual(len(self.cart.items), 0)

class TestStore(unittest.TestCase):
    def setUp(self):
        self.store = code_from_test.Store()
        self.user = code_from_test.User("John Doe", "john@example.com")
        self.product = code_from_test.Product("Test Product", 100, 10)
        
    def test_store_initialization(self):
        self.assertEqual(len(self.store.products), 0)
        self.assertEqual(len(self.store.users), 0)
        
    def test_add_product(self):
        self.store.add_product(self.product)
        self.assertIn(self.product, self.store.products)
        
    def test_register_user(self):
        self.store.register_user(self.user)
        self.assertIn(self.user, self.store.users)
        
    def test_find_user_success(self):
        self.store.register_user(self.user)
        found_user = self.store.find_user("john@example.com")
        self.assertEqual(found_user, self.user)
        
    def test_find_user_failure(self):
        found_user = self.store.find_user("nonexistent@example.com")
        self.assertIsNone(found_user)

if __name__ == '__main__':
    unittest.main()