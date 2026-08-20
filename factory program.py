class PaymentStrategy:
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


class PaymentProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("Please select a payment method.")
        else:
            self.strategy.pay(amount)


processor = PaymentProcessor()

processor.set_strategy(CreditCardPayment())
processor.process_payment(1000)

processor.set_strategy(UPIPayment())
processor.process_payment(500)

processor.set_strategy(PayPalPayment())
processor.process_payment(750)