import unittest
from user import User
from warehouse import Warehouse

class WarehouseTest(unittest.TestCase):

    def test_warehouse_displays_correct_stock(self):
        warehouse = Warehouse(2, 2, 2)
        warehouse2 = Warehouse(0, 0, 0)

        self.assertEqual(warehouse.pants_quantity, 2)
        self.assertEqual(warehouse.shoes_quantity, 2)
        self.assertEqual(warehouse.jackets_quantity, 2)

        self.assertEqual(warehouse2.pants_quantity, 0)
        self.assertEqual(warehouse2.shoes_quantity, 0)
        self.assertEqual(warehouse2.jackets_quantity, 0)


    def test_warehouse_when_buying_more_than_available_stock(self):
        shoes_quantity = 2
        pants_quantity = 5
        jackets_quantity = 10
        shoes_price = 20.0
        pants_price = 50.0
        jackets_price = 100.0
        warehouse = Warehouse(shoes_quantity, pants_quantity, jackets_quantity, shoes_price, pants_price, jackets_price)

        self.assertEqual(warehouse.buy_shoes(5, None), 0)
        self.assertEqual(warehouse.buy_pants(20, None), 0)
        self.assertEqual(warehouse.buy_jacket(20, None), 0)


    def test_warehouse_for_correct_price(self):
        customer = User("Mike", 1500)
        shoes_price = 20.0
        pants_price = 50.0
        jackets_price = 100.0
        warehouse = Warehouse(2, 5, 10, shoes_price, pants_price, jackets_price)

        self.assertEqual(warehouse.buy_shoes(2, customer), 40.0)
        self.assertEqual(warehouse.buy_pants(5, customer), 250.0)
        self.assertEqual(warehouse.buy_jacket(10, customer), 850.0)


    def test_warehouse_applied_discount_if_10_items(self):
        customer = User("Mike", 1500)
        shoes_price = 10
        pants_price = 20
        jackets_price = 30
        shoes_quantity = 10
        pants_quantity = 10
        jackets_quantity = 10
        warehouse = Warehouse(shoes_quantity, pants_quantity, jackets_quantity, shoes_price, pants_price, jackets_price)

        self.assertEqual(warehouse.buy_shoes(10, customer), 85)
        self.assertEqual(warehouse.buy_pants(10, customer), 170)
        self.assertEqual(warehouse.buy_jacket(10, customer), 255)


    def test_warehouse_applied_discount_if_user_subscribed(self):
        customer = User("Mark", 1000, True)
        shoes_price = 10
        pants_price = 20
        jackets_price = 30
        shoes_quantity = 20
        pants_quantity = 20
        jackets_quantity = 20
        warehouse = Warehouse(shoes_quantity, pants_quantity, jackets_quantity, shoes_price, pants_price, jackets_price)

        self.assertEqual(warehouse.buy_shoes(5, customer), 40)
        self.assertEqual(warehouse.buy_pants(5, customer), 80)
        self.assertEqual(warehouse.buy_jacket(5, customer), 120)

        self.assertEqual(warehouse.buy_shoes(10, customer), 68)
        self.assertEqual(warehouse.buy_pants(10, customer), 136)
        self.assertEqual(warehouse.buy_jacket(10, customer), 204)


    def test_warehouse_user_lacking_balance(self):
        customer = User("Mark", 99, False)
        shoes_price = 100
        pants_price = 200
        jackets_price = 300
        shoes_quantity = 1
        pants_quantity = 1
        jackets_quantity = 1
        warehouse = Warehouse(shoes_quantity, pants_quantity, jackets_quantity, shoes_price, pants_price, jackets_price) 

        self.assertEqual(warehouse.buy_shoes(1, customer), 0)
        self.assertEqual(warehouse.buy_pants(1, customer), 0)
        self.assertEqual(warehouse.buy_jacket(1, customer), 0)       



class UserTest(unittest.TestCase):

    def test_correct_user_balance_after_purchase(self):
        customer = User("Mark", 10000, False)
        shoes_price = 100
        pants_price = 200
        jackets_price = 300
        shoes_quantity = 10
        pants_quantity = 10
        jackets_quantity = 10
        warehouse = Warehouse(shoes_quantity, pants_quantity, jackets_quantity, shoes_price, pants_price, jackets_price) 

        self.assertEqual(customer.checkout(warehouse.buy_shoes(5, customer)), 9500)
        self.assertEqual(customer.checkout(warehouse.buy_pants(3, customer)), 8900)
        self.assertEqual(customer.checkout(warehouse.buy_jacket(3, customer)), 8000)

    
    def test_correct_user_balance_after_purchase_with_subscription(self):
        customer = User("Mark", 10000, True)
        shoes_price = 100
        pants_price = 200
        jackets_price = 300
        shoes_quantity = 10
        pants_quantity = 10
        jackets_quantity = 10
        warehouse = Warehouse(shoes_quantity, pants_quantity, jackets_quantity, shoes_price, pants_price, jackets_price)  

        self.assertEqual(customer.checkout(warehouse.buy_shoes(5, customer)), 9600)
        self.assertEqual(customer.checkout(warehouse.buy_pants(3, customer)), 9120)
        self.assertEqual(customer.checkout(warehouse.buy_jacket(3, customer)), 8400)     


    def test_correct_user_balance_after_purchase_with_subscription_and_quantity_discount(self):
        customer = User("Mark", 10000, True)
        shoes_price = 100
        pants_price = 200
        jackets_price = 300
        shoes_quantity = 20
        pants_quantity = 20
        jackets_quantity = 20
        warehouse = Warehouse(shoes_quantity, pants_quantity, jackets_quantity, shoes_price, pants_price, jackets_price)  

        self.assertEqual(customer.checkout(warehouse.buy_shoes(10, customer)), 9320)
        self.assertEqual(customer.checkout(warehouse.buy_pants(12, customer)), 7688)
        self.assertEqual(customer.checkout(warehouse.buy_jacket(20, customer)), 3608)    


    def test_user_buy_subscription_with_no_balance(self):
        customer = User("Mark", 0, False)

        self.assertEqual(customer.upgrade_account(), False)



if __name__ == '__main__':
    unittest.main()