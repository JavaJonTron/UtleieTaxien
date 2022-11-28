class PaymentOrder:
    def __init__(self, paid_amount, date_approved=None, booking=None):
        self.paid_amount = paid_amount
        self.date_approved = date_approved
        self.booking = booking
        self.reserved_amount = 0

    def payment_reservation(self):
        if self.reserved_amount == 0:
            self.reserved_amount = self.paid_amount

        if self.reserved_amount > 0:
            self.booking.renter.wallet.remove_from_wallet(amount=self.paid_amount)

    def payment_refund(self):
        self.booking.renter.wallet.add_to_wallet(self.reserved_amount)
        self.reserved_amount -= self.reserved_amount


    def payment_processing(self):
        self.reserved_amount -= self.reserved_amount
