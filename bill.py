from datetime import date

class Bill:
    def __init__(self, user, items):
        self.user = user
        self.items = items
        self.bill_date = date.today()
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

    def print_bill(self):
        print("Bill Details:")
        print(f"User: {self.user.name}")
        print(f"Bill Date: {self.bill_date}")
        print("\nMedicine List:")
        for item in self.items:
            print(f"- {item.name} (x{item.quantity}): ₹{item.price:.2f}")
        print(f"\nTotal Amount: ₹{self.total_amount:.2f}")
