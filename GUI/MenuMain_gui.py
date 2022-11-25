from dearpygui import dearpygui as dpg

import Car.create_car_file
import main
import owner.owner
import renter.renter
from functions import delete_windows
from Booking import create_booking_file
from functions import get_todays_date as date
from functions import log_off_func
from functions import logged_in_status_file
from main import bookings_list
from main import renter_list
from main import car_list
from main import owner_list

dpg.create_context()
dpg.create_viewport(title='Utleie_app', width=600, height=600)

def admin_login():
    '''
    Denne kodenblokken tar for seg Admin innlogging og sender brukeren vidre til admin control panel
    :return:
    '''
    dpg.delete_item("Admin Login")
    dpg.delete_item("Main menu")
    with dpg.window(label="Admin Login", tag="Admin Login", width=300, height=200):
        dpg.set_primary_window("Admin Login", True)
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Admin username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Admin password")
        dpg.add_button(label="Log in", tag="adminLogInButton", callback=log_in_accepted)

def owner_login():
    '''
    Denne kodenblokken tar for seg Owner innlogging og sender brukeren vidre til owner control panel.
    For prototypen har vi hardprogrammert inn to forskjellige eiere som man kan velge å logge seg inn som
    :return:
    '''
    dpg.delete_item("Owner Login")
    dpg.delete_item("Main menu")
    with dpg.window(label="Owner Login", tag="Owner Login", width=300, height=200):
        dpg.set_primary_window("Owner Login", True)
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Owner username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Owner password")
        dpg.add_button(label="Owner 1 Log in", tag="owner1LogInButton", callback=log_in_accepted,
                       user_data=owner_list[0])
        dpg.add_button(label="Owner 2 Log in", tag="owner2LogInButton", callback=log_in_accepted,
                       user_data=owner_list[1])
        dpg.add_button(label="Owner Log in with Google", tag="ownerLogInGoogleButton")
        dpg.add_button(label="Owner Log in with Vipps", tag="ownerLogInVippsButton")

def renter_login():
    '''
    Denne kodenblokken tar for seg Renter innlogging og sender brukeren vidre til renter control panel.
    For prototypen har vi hardprogrammert inn to forskjellige leiere som man kan velge å logge seg inn som.
    Man kan også logge seg inn med Google eller Vipps (ikke reel innlogging og er deaktivert for prototypen)
    :return:
    '''
    dpg.delete_item("Renter Login")
    dpg.delete_item("Main menu")
    with dpg.window(label="Renter Login", tag="Renter Login", width=300, height=200):
        dpg.set_primary_window("Renter Login", True)
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Renter username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Renter password")
        dpg.add_button(label="Renter 1 Log in", tag="renter1LogInButton", callback=log_in_accepted,
                       user_data=renter_list[0])
        dpg.add_button(label="Renter 2 Log in", tag="renter2LogInButton", callback=log_in_accepted,
                       user_data=renter_list[1])
        dpg.add_button(label="Renter Log in", tag="renterLogInButton")
        dpg.add_button(label="Renter Log in with Google", tag="renterLogInGoogleButton")
        dpg.add_button(label="Renter Log in with Vipps", tag="renterLogInVippsButton")

def main_menu():
    '''
    Dette er vinduet som møter deg ved programstart og lar bruker velge hvilken rolle man skal logge seg inn som
    :return:
    '''
    with dpg.window(label="Main menu", tag="Main menu"):
        dpg.add_text("Log in")
        dpg.add_button(label="Log in as renter", tag="renterLogin", callback=renter_login)
        dpg.add_button(label="Log in as owner", tag="ownerLogin", callback=owner_login)
        dpg.add_button(label="Log in as admin", tag="adminLogin", callback=admin_login)
        dpg.set_primary_window("Main menu", True)


main_menu()

def log_out(sender=None, app_data=None, user_data=None):
    '''
    Denne funksjonen tar for seg utlogging av brukere, den sletter alle vinduer og setter brukere til avlogget.
    Så kaller den på starten av programmet
    :return:
    '''
    delete_windows.delete_windows_func()
    log_off_func.log_off_human(user_data)
    #NÅ LOOPER DEN IGJENNOM LISTA, OG LOGGER AV ALLE.
    #KANSJE LEGGE INN OBEJKTET SOM SKAL LOGGES UT I PARAMETER FELTET
    #ISTEDENFOR Å LOGGE AV ALLE I EN BESTEMT LISTE?
    main_menu()

def log_in_accepted(sender, app_data, user_data):
    '''
    Denne tar for seg innlogging av brukere og sjekker hvilken innlogging som gjelder
    :param sender: ikke i bruk
    :param app_data: ikke i bruk
    :param user_data: Bruker data, altså hvilken bruker som er logget inn
    :return:
    '''
    delete_windows.delete_windows_func()
    log_off_func.log_off_human(renter_list)
    log_off_func.log_off_human(owner_list)
    logged_in_user = user_data
    logged_in_user.is_logged_in = True

    if checking_object_instance(logged_in_user, renter.renter.Renter):
        welcome_screen_renter(user_data=logged_in_user)
        print("YOU ARE LOGGED IN AS A RENTER")

    if checking_object_instance(logged_in_user, owner.owner.Owner):
        welcome_screen_owner(user_data=logged_in_user)
        print("YOU ARE LOGGED IN AS AN OWNER")

def checking_object_instance(object_type, class_type):
    '''
    Sjekker om et object er av en type klasse.
    :param object_type: Bruker som er innolgget
    :param class_type: Klassen som er i bruk
    :return: True eller False om et object er en klasse
    '''
    if isinstance(object_type, class_type):
        return True
    else:
        return False

def welcome_screen_renter(sender=None, app_data=None, user_data=None):
    '''
    Bekreftelse til bruker på at h*n er innlogget som en renter
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Innlogget bruker
    :return:
    '''
    with dpg.window(label="Renter Control Panel", tag="Renter Login Accepted", width=400, height=400):
        dpg.set_primary_window("Renter Login Accepted", True)
        dpg.add_text(f"Successfully logged in as {user_data.name}")
        dpg.add_button(label="Click me to continue", callback=renter_main_menu, user_data=user_data)

def welcome_screen_owner(sender=None, app_data=None, user_data=None):
    '''
    Bekreftelse til bruker på at h*n er innlogget som en owner
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Innlogget bruker
    :return:
    '''
    with dpg.window(label="Owner Control Panel", tag="Owner Login Accepted", width=400, height=400):
        dpg.set_primary_window("Owner Login Accepted", True)
        dpg.add_text(f"Successfully logged in as {user_data.name}")
        dpg.add_button(label="Click me to continue", callback=owner_main_menu, user_data=user_data)

def welcome_screen_admin(sender=None, app_data=None, user_data=None):
    '''
    Bekreftelse til bruker på at h*n er innlogget som en admin
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Innlogget bruker
    :return:
    '''
    with dpg.window(label="Admin Control Panel", tag="Admin Login Accepted", width=400, height=400):
        dpg.set_primary_window("Admin Login Accepted", True)
        dpg.add_text(f"Successfully logged in as {user_data.name}")
    # dpg.add_button(label="Click me to continue", callback=admin_main_menu, user_data=user_data)
    # DEN OVER MÅ JEG LEGGE TIL IGJEN NÅR JEG HAR OPPRETTET admin_main_menu,

def owner_main_menu(sender, app_data, user_data):
    '''
    Main menu for eiere, her kan man navigere til forskjellige sider og velge hva man ønsker å gjøre
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Innlogget bruker
    :return:
    '''
    logged_in_user = logged_in_status_file.logged_in_status(owner_list)
    delete_windows.delete_windows_func()
    with dpg.window(label="Owner Control Panel", tag="Owner Main", width=400, height=400):
        dpg.set_primary_window("Owner Main", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=owner_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Add a new car", callback=new_car, user_data=logged_in_user)
            dpg.add_menu_item(label="See my cars", callback=see_cars, user_data=logged_in_user)
            dpg.add_menu_item(label="Options", callback=owner_options, user_data=logged_in_user)
            dpg.add_menu_item(label="approve/deny bookings", callback=approve_deny_bookings, user_data=user_data)
            dpg.add_button(label="Log Out", callback=log_out, user_data=owner_list)
        dpg.add_text("Main menu", tag="renterMainMenuText")

def renter_main_menu(sender, app_data, user_data):
    '''
    Main menu for renter, her kan man navigere til forskjellige sider og velge hva man ønsker å gjøre
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Innlogget bruker
    :return:
    '''
    delete_windows.delete_windows_func()
    logged_in_user = user_data
    with dpg.window(label="Renter Control Panel", tag="Renter Main", width=400, height=400):
        dpg.set_primary_window("Renter Main", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=renter_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Rent a new car", callback=rent_new_car, user_data=logged_in_user)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars, user_data=logged_in_user)
            dpg.add_menu_item(label="Options", callback=renter_options, user_data=logged_in_user)
            dpg.add_button(label="Log Out", callback=log_out, user_data=renter_list)
        dpg.add_text("Main menu", tag="renterMainMenuText")

def approve_deny_bookings(sender=None, app_data=None, user_data=None):
    '''
    Denne funksjonen gir eiere en oversikt over bookinger som leiere ønsker å gjøre. Eiere kan klikke seg inn på
    bookingene
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Innlogget bruker
    :return:
    '''
    logged_in_user = logged_in_status_file.logged_in_status(owner_list)
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Approve Or Deny", width=400, height=400):
        dpg.set_primary_window("Approve Or Deny", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=owner_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Log Out", callback=log_out, user_data=owner_list)
        for bookings in bookings_list:
            if bookings.car.owner.name == user_data.name:
                if bookings.approved == False:
                    label_text = "Car: " + bookings.car.nickname() + " From: " + str(bookings.date_from['Day']) + "." + \
                                 str(bookings.date_from['Month']) + "." + str(bookings.date_from['Year']) + " To: " + \
                                 str(bookings.date_to['Day']) + "." + str(bookings.date_to['Month']) + "." + \
                                 str(bookings.date_to['Year'])
                    dpg.add_button(label=label_text, callback=approve_car, user_data=bookings)

def approve_car(sender, app_data, user_data=None):
    '''
    Lar eieren godkjenne bookingen eieren klikket seg inn på i en tidligere funksjon
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Booking
    :return:
    '''
    booking = user_data
    delete_windows.delete_windows_func()
    logged_in_user = logged_in_status_file.logged_in_status(owner_list)
    with dpg.window(label="Owner Control Panel", tag="Approve Car", width=400, height=400):
        dpg.set_primary_window("Approve Car", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=owner_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Log Out", callback=log_out, user_data=owner_list)
        dpg.add_text(booking.renter.name + " wants to rent your " + booking.car.nickname() + " with license plate " +
                     booking.car.license_plate)
        dpg.add_text(booking.renter.name + " wants to rent it from " + str(booking.date_from['Day']) + "." + \
                     str(booking.date_from['Month']) + "." + str(booking.date_from['Year']) + " to: " + \
                     str(booking.date_to['Day']) + "." + str(booking.date_to['Month']) + "." + \
                     str(booking.date_to['Year']))
        dpg.add_text(booking.renter.name + "s score is " + str(booking.renter.score) + " out of X")
        dpg.add_button(label="Approve", callback=approved_booking, user_data=booking)
        dpg.add_button(label="Deny", callback=denied_booking, user_data=booking)

def approved_booking(sender, app_data, user_data):
    '''
    FUnkjsonen setter bookingen til godkjent når eieren klikker på approve i tidligere funksjon
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Booking
    :return:
    '''
    logged_in_user = logged_in_status_file.logged_in_status(owner_list)
    booking = user_data
    for bookings in bookings_list:
        if booking == bookings:
            booking.approved = True
    delete_windows.delete_windows_func()
    approve_deny_bookings(user_data=logged_in_user)

def denied_booking(sender, app_data, user_data):
    '''
    Funksjonen setter bookingen til ikke godkjent og sletter den når eieren klikker på deny i tidligere funksjon
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Booking
    :return:
    '''
    logged_in_user = logged_in_status_file.logged_in_status(owner_list)
    booking = user_data
    for bookings in bookings_list:
        if booking == bookings:
            print(f"{bookings_list.remove(booking)}")
            booking.approved = False
    delete_windows.delete_windows_func()
    approve_deny_bookings(user_data=logged_in_user)

def new_car(sender, app_data, user_data):
    '''
    Denne tar for seg opprettelse av nye biler når eieren ønsker å legge til ny. Ikke i bruk nå.
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Ikke i bruk
    :return:
    '''
    logged_in_user = logged_in_status_file.logged_in_status(owner_list)
    delete_windows.delete_windows_func()
    with dpg.window(label="Owner Control Panel", tag="Owner New Car", width=400, height=400):
        dpg.set_primary_window("Owner New Car", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=owner_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Log Out", callback=log_out, user_data=owner_list)
        dpg.add_text("Fill out all fields to add a new car")
        dpg.add_input_text(hint="Make:", tag="make", no_spaces=True, uppercase=True, label="Make")
        dpg.add_input_text(hint="Model:", tag="model", uppercase=True, label="Model")
        dpg.add_input_int(min_value=2000, max_value=date.year, default_value=2016, tag="year", label="Year")
        dpg.add_input_text(hint="License Plate", tag="license_plate", no_spaces=True, uppercase=True, label="License Plate")
        dpg.add_input_text(hint="Fuel Source:", tag="fuel_source", no_spaces=True, uppercase=True, label="Fuel Source")
        dpg.add_input_int(min_value=0, label="Odometer", tag="odometer")
        dpg.add_input_int(min_value=0, label="Hourly Rate", tag="hourly")
        dpg.add_input_int(min_value=0, label="Daily rate", tag="daily")
        dpg.add_button(label="Publish", callback=create_car_redirect)

def create_car_redirect(sender, app_data, user_data):
    Car.create_car_file.create_car()
    owner_main_menu(sender=None, app_data=None, user_data=None)


def see_cars(sender, app_data, user_data):
    '''
    Viser eieren bilene h*n har til utleie
    :param sender: Ikke i bruk
    :param app_data: Ikke i bruk
    :param user_data: Logged in user
    :return:
    '''
    logged_in_user = logged_in_status_file.logged_in_status(owner_list)
    delete_windows.delete_windows_func()
    with dpg.window(label="Owner Control Panel", tag="Owner See Cars", width=400, height=400):
        dpg.set_primary_window("Owner See Cars", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=owner_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Log Out", callback=log_out, user_data=owner_list)
        for car in car_list:
            if car.owner.name == user_data.name:
                dpg.add_button(label=car.nickname(), callback=see_detailed_car_info, user_data=car)
        dpg.add_text("See owned cars")

def see_detailed_car_info(sender, app_data, user_data):
    logged_in_user = logged_in_status_file.logged_in_status(owner_list)
    delete_windows.delete_windows_func()
    with dpg.window(label="Owner Control Panel", tag="Owner See Detailed Cars", width=400, height=400):
        dpg.set_primary_window("Owner See Detailed Cars", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=owner_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Log Out", callback=log_out, user_data=owner_list)
        dpg.add_text(user_data.nickname())
        dpg.add_text(f"Make: {user_data.make}")
        dpg.add_text(f"Model: {user_data.model}")
        dpg.add_text(f"Year: {user_data.year}")
        dpg.add_text(f"License plate: {user_data.license_plate}")
        dpg.add_text(f"Fuel Source: {user_data.fuel_source}")
        dpg.add_text(f"Odometer: {user_data.km}")
        dpg.add_text(f"Hourly Rate: {user_data.hourly_rate}kr")
        dpg.add_text(f"Daily Rate: {user_data.daily_rate}kr")
        dpg.add_text(f"Earned total: {user_data.earned_total}kr")
        dpg.add_button(label="Delete car", callback=delete_car, user_data=user_data)

def delete_car(sender, app_data, user_data):
    logged_in_user = logged_in_status_file.logged_in_status(owner_list)
    car_list.remove(user_data)
    main.save_system('car_file', car_list)
    owner_main_menu(sender=None, app_data=None, user_data=logged_in_user)

def render_cars():
    '''
    Denne funksjonen legger bilene i knapper for brukeren å klikke på
    :return:
    '''
    for bil in car_list:
        dpg.add_button(label=bil.nickname(), callback=car, user_data=bil)

def rent_new_car(sender, app_data, user_data):
    '''
    Her
    :param sender:
    :param app_data:
    :param user_data:
    :return:
    '''
    logged_in_user = logged_in_status_file.logged_in_status(renter_list)
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter New Car", width=400, height=400):
        dpg.set_primary_window("Renter New Car", True)
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=renter_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Log Out", callback=log_out, user_data=renter_list)
        render_cars()
        dpg.add_text("Rent new car")

def car(sender, app_data, user_data):
    '''
    Her vil user_data ta for seg et renter objekt.
    Her vil funksjonen ta for seg leiers mulighet til å leie en bil.
    Det vil også være et eget view som opprettes her for å kunne
    se biler som ikke er tilgjengelige
    Denne funksjonen kan bli kalt fra funksjonen render_cars
    :param sender:
    :param app_data:
    :param user_data:
    :return:
    '''
    logged_in_user = logged_in_status_file.logged_in_status(renter_list)
    avail_list = []
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter Car", width=400, height=400):
        dpg.set_primary_window("Renter Car", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=renter_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Log Out", callback=log_out, user_data=renter_list)
        dpg.add_text(user_data.nickname())
        dpg.add_text(f"Owner: {user_data.owner.name}")
        dpg.add_text(f"Fuel Source: {user_data.fuel_source}")
        dpg.add_text(f"Hourly Rate: {user_data.hourly_rate}kr")
        dpg.add_text(f"Daily Rate: {user_data.daily_rate}kr")
        dpg.add_text("FROM DATE:")
        dpg.add_date_picker(tag="from_date", default_value={'month_day': date.day, 'year': date.year, 'month': date.
                            month}, callback=create_booking_file.dates_from)
        dpg.add_text("TO DATE:")
        dpg.add_date_picker(tag="to_date", default_value={'month_day': date.day + 1, 'year': date.year, 'month': date.
                            month}, callback=create_booking_file.dates_to)
        dpg.add_button(label="Book", callback=create_booking_file.booking_func, user_data=user_data)
        dpg.add_text("Car is not available between:")
        for booking in bookings_list:
            if booking.car.license_plate == user_data.license_plate:
                if booking.approved:
                    date_from_day = booking.date_from["Day"]
                    date_from_month = booking.date_from["Month"]
                    date_from_year = booking.date_from["Year"]
                    date_to_day = booking.date_to["Day"]
                    date_to_month = booking.date_to["Month"]
                    date_to_year = booking.date_to["Year"]
                    avail_list.append(
                        f"{date_from_day}.{date_from_month}.{date_from_year} - {date_to_day}.{date_to_month}.{date_to_year}")
        dpg.add_listbox(tag="dates", items=avail_list)

def see_rented_cars(sender, app_data, user_data):
    '''
    Her så vil user_data tilsvare et renter objekt
    Det funksjonen tar for seg er Leiers mulighet til å se biler han/hun har leid.
    Denne funksjonen kan bli kalt fra renter_main_menu
    :param sender:
    :param app_data:
    :param user_data:
    :return:
    '''
    logged_in_user = logged_in_status_file.logged_in_status(owner_list)
    rented_cars = []
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter See Cars", width=400, height=400):
        dpg.set_primary_window("Renter See Cars", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=renter_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Log Out", callback=log_out, user_data=renter_list)
        for booking in bookings_list:
            if booking.approved:
                if booking.renter.name == user_data.name:
                    rented_cars.append(
                        f"{booking.car.nickname()}, {booking.date_from['Day']}.{booking.date_from['Month']}."
                        f"{booking.date_from['Year']}-{booking.date_to['Day']}.{booking.date_to['Month']}."
                        f"{booking.date_to['Year']}")
        dpg.add_listbox(tag="rented", items=rented_cars)
        dpg.add_text("See rented cars")

def renter_options():
    '''
    Denne funksjonen skal ta for seg det som er Leiers alternativer på kontosiden.
    Denne funksjonen kan bli kalt fra renter_main_menu
    :return:
    '''
    logged_in_user = logged_in_status_file.logged_in_status(renter_list)
    delete_windows.delete_windows_func()
    with dpg.window(label="Renter Control Panel", tag="Renter Options", width=400, height=400):
        dpg.set_primary_window("Renter Options", True)
        with dpg.menu_bar(label="Menu Bar"):
            dpg.add_button(label="Home", callback=renter_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Log Out", callback=log_out, user_data=renter_list)
        dpg.add_text("Options")

def owner_options():
    '''
    Denne funksjonen skal ta for seg det som er Utleiers alternativer på kontosiden.
    Denne kan bli kalt fra [owner_main_menu]
    :return:
    '''
    logged_in_user = logged_in_status_file.logged_in_status(owner_list)
    delete_windows.delete_windows_func()
    with dpg.window(label="Owner Control Panel", tag="Owner Options", width=400, height=400):
        dpg.set_primary_window("Owner Options", True)
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=owner_main_menu, user_data=logged_in_user)
            dpg.add_button(label="Log Out", callback=log_out, user_data=owner_list)
        dpg.add_text("Options")

# def admin_options():
#    delete_windows.delete_windows_func()
#    with dpg.window(label="Admin Control Panel", tag="Admin Options", width=400, height=400):
#        dpg.set_primary_window("Admin Options", True)
#        with dpg.menu_bar(label="Menu Bar"):
# dpg.add_menu_item(label="Rent a new car")
# dpg.add_button(label="Home", callback=admin_main_menu)
#       dpg.add_text("Options")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
