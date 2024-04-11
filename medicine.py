from datetime import date, timedelta
import random

class Medicine:
    def __init__(self, name, quantity):
        self.name = name
        self.price = random.uniform(1, 1000)  # Random price between 1 and 1000
        self.mfd = date.today()
        self.exp = self.mfd + timedelta(days=365 * 3)  # Assuming a fixed 3 years expiry
        self.power = random.randint(1, 10) * 100  # Random multiple of 100 between 100 and 1000
        self.quantity = quantity
