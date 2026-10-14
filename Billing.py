class Bill:
    def _init_(self, customer_name, bill_number, bill_amount):
        self.customer_name = customer_name
        self.bill_number = bill_number
        self.bill_amount = bill_amount

    def get_category(self):
        if self.bill_amount >= 5000:
            return "High Value"
        elif self.bill_amount >= 1000:
            return "Medium Value"
        else:
            return "Low Value"

    def display(self):
        print(self)

    def _str_(self):
        return self.customer_name + " | " + self.bill_number + " | " + str(self.bill_amount) + " | " + self.get_category()


class Pharmacy:
    def _init_(self):
        self.bills = []

    def add_bill(self, bill):
        self.bills.append(bill)

    def display_all(self):
        for bill in self.bills:
            bill.display()


n = int(input( ))

pharmacy = Pharmacy()

for i in range(n):
    data = input().split(",")
    customer_name = data[0]
    bill_number = data[1]
    bill_amount = int(data[2])

    bill = Bill(customer_name, bill_number, bill_amount)
    pharmacy.add_bill(bill)

pharmacy.display_all()