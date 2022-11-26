
def approved_or_deny_booking(booking, decision, list_of_bookings):
    for bookings in list_of_bookings:
        if booking == bookings:
            if not decision:
                print("YES NÅ BLIR DENNE FUNKSJONEN KALT PÅ FALSE")
                booking.approved = decision
                print(f"{list_of_bookings.remove(booking)}")
                return decision
            elif decision:
                print("YES NÅ BLIR DENNE FUNKSJONEN KALT PÅ TRUE")
                booking.approved = decision
                booking.order.payment_processing()
                return decision
