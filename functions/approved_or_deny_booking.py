def approved_or_deny_booking(booking, decision, list_of_bookings):
    """
    Denne endret approved attributtet i et booking object til approved om eiere velger å godkjenne bookingen, hvis ikke
    sletter den bookingen
    :param booking: Booking objectet
    :param decision: Avgjørelsen til eier
    :param list_of_bookings: Liste med alle bookinger
    :return: Avgjørelsen til eier
    """
    for bookings in list_of_bookings:
        if booking == bookings:
            if not decision:
                booking.approved = decision
                print(f"{list_of_bookings.remove(booking)}")
                return decision
            elif decision:
                booking.approved = decision
                return decision
