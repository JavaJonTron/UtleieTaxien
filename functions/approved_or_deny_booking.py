from main import bookings_list

def approved_or_deny_booking(booking, decision):
    for bookings in bookings_list:
        if booking == bookings:
            if not decision:
                print("YES NÅ BLIR DENNE FUNKSJONEN KALT PÅ FALSE")
                booking.approved = decision
                print(f"{bookings_list.remove(booking)}")
                return decision
            elif decision:
                print("YES NÅ BLIR DENNE FUNKSJONEN KALT PÅ TRUE")
                booking.approved = decision
                return decision
