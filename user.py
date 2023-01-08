class User:
    def __init__(self, name: str, balance = 0.0, subscription = False):
        self.name = name
        self._balance = balance
        self._subscription = subscription


    @property
    def subscription(self):
        return self._subscription

    @subscription.setter
    def subscription(self, value):
        self._subscription = value


    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, new_amount):
        self._balance = new_amount


    def checkout(self, bill):
        self.balance -= bill
        print(f"Your current balance is €{round(self.balance, 2)}")
        return self.balance


    def upgrade_account(self):
        if self.balance >= 10.0:
            self.subscription = True
            self.balance -= 10.0
            print("You have just upgraded your account to PLUS for €10.00")
        else:
            print("Sorry, insufficient funds.")
            return False


    def __repr__(self):
        return f"\n####\nUser's name: {self.name}, with balance of €{round(self.balance, 2)}. Subscribed: {self.subscription}\n####\n"


    