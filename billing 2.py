class Bill:
    def __init__(self, customer_name, bill_number, bill_amount):
        self.customer_name = customer_name
        self.bill_number = bill_number
        self.bill_amount = bill_amount

    def display(self):
        print(f"Customer: {self.customer_name}, Bill No: {self.bill_number}, Amount: {self.bill_amount}")


class Pharmacy:
    def __init__(self):  # Fixed: Changed _init_ to __init__
        self.bills = []

    def add_bill(self, bill):
        self.bills.append(bill)

    def display_all(self):
        for bill in self.bills:
            bill.display()


# --- execution ---
n = int(input())
pharmacy = Pharmacy()

for i in range(n):
    data = input().split(",")
    customer_name = data[0]
    bill_number = data[1]
    bill_amount = int(data[2])

    bill = Bill(customer_name, bill_number, bill_amount)
    pharmacy.add_bill(bill)

pharmacy.display_all()
