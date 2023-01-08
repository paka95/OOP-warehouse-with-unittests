class Warehouse:
    def __init__(self, shoes_quantity, pants_quantity, jackets_quantity, shoes_price = 99.99, pants_price = 76.95, jackets_price = 129.99):
        self.shoes_quantity = shoes_quantity
        self.pants_quantity = pants_quantity
        self.jackets_quantity = jackets_quantity
        self._shoes_price = shoes_price
        self._pants_price = pants_price
        self._jackets_price = jackets_price


    @property
    def shoes_price(self):
        return self._shoes_price

    @shoes_price.setter
    def shoes_price(self, new_shoes_price):
        self._shoes_price = new_shoes_price


    @property
    def pants_price(self):
        return self._pants_price

    @pants_price.setter
    def pants_price(self, new_pants_price):
        self._pants_price = new_pants_price

    
    @property
    def jackets_price(self):
        return self._jackets_price

    @jackets_price.setter
    def jackets_price(self, new_jackets_price):
        self._jackets_price = new_jackets_price


    @staticmethod
    def apply_quantity_discount(price, quantity):
        discounted_price = (price * quantity) * 0.85
        print("Applied 15% quantity discount!")
        return discounted_price


    @staticmethod
    def apply_subscription_discount(total_price):
        total_price *= 0.8
        print("Applied 20% subscription discount!")
        return total_price


    def buy_shoes(self, quantity, user):
        if self.shoes_quantity >= quantity:
            total_price = self.shoes_price * quantity
            if user.balance >= total_price:
                if quantity >= 10:
                    total_price = Warehouse.apply_quantity_discount(self.shoes_price, quantity)
                
                if user.subscription == True:
                    total_price = Warehouse.apply_subscription_discount(total_price)
                print(f"Bought {quantity} shoes for €{round(total_price, 2)}!")
                self.shoes_quantity -= quantity
                return total_price
            else:
                print("Not enough money, sorry!")
                return 0
        else:
            print("Not enough shoes in stock, sorry!")
            return 0



    def buy_pants(self, quantity, user):
        if self.pants_quantity >= quantity:
            
            total_price = self.pants_price * quantity
            if user.balance >= total_price:
                if quantity >= 10:
                    total_price = Warehouse.apply_quantity_discount(self.pants_price, quantity)
                
                if user.subscription == True:
                    total_price = Warehouse.apply_subscription_discount(total_price)
                print(f"Bought {quantity} pants for €{round(total_price, 2)}!")
                self.pants_quantity -= quantity
                return total_price
            else:
                print("Not enough money, sorry!")
                return 0
        else:
            print("Not enough pants in stock, sorry!")
            return 0


    def buy_jacket(self, quantity, user):
        if self.jackets_quantity >= quantity:

            total_price = self.jackets_price * quantity
            if user.balance >= total_price:
                if quantity >= 10:
                    total_price = Warehouse.apply_quantity_discount(self.jackets_price, quantity)
                
                if user.subscription == True:
                    total_price = Warehouse.apply_subscription_discount(total_price)
                print(f"Bought {quantity} jackets for €{round(total_price, 2)}!")
                self.jackets_quantity -= quantity
                return total_price
            else:
                print("Not enough money, sorry!")
                return 0
        else:
            print("Not enough jackets in stock, sorry!")
            return 0



    def __repr__(self):
        return f"Currently we have {self.shoes_quantity} shoes, {self.pants_quantity} pants and {self.jackets_quantity} jackets!"