class PaymentOrder:
    def __init__(self, amount, date_approved=None, booking=None):
        self.amount = amount
        self.date_approved = date_approved
        self.booking = booking

    def payment_processing(self):
        self.booking.renter.remove_from_wallet(amount=self.amount)
        print(f'THIS MUCH WAS PAID {self.amount}')
        print(f'THIS MUCH IS LEFT{self.booking.renter.wallet}')
