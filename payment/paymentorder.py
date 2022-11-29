class PaymentOrder:
    def __init__(self, paid_amount, date_approved=None, booking=None):
        self.paid_amount = paid_amount
        self.date_approved = date_approved
        self.booking = booking
        self.reserved_amount = 0

    def payment_reservation(self):
        """
        Her blir pengene trukket fra Leiers konto og reservert.
        Dette skjer når Leier utfører en booking forespørsel.

        :return:
        """
        if self.reserved_amount == 0:
            self.reserved_amount = self.paid_amount

        if self.reserved_amount > 0:
            self.booking.renter.wallet.remove_from_wallet(amount=self.paid_amount)

    def payment_refund(self):
        """
        Her vil pengene gå tilbake til Leiers konto dersom h*n avslår leieforespørselen

        :return:
        """
        self.booking.renter.wallet.add_to_wallet(self.reserved_amount)
        self.reserved_amount -= self.reserved_amount

    def payment_processing(self):
        """
        Her så sletter man den reserverte pengesummen.
        Det er da en antagelse at pengene går inn på utleiers konto.
        :return:
        """
        self.reserved_amount -= self.reserved_amount
