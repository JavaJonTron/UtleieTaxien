import dearpygui.dearpygui as dpg

def log_in_accepted():
    dpg.delete_item("Renter Control Panel")
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
        dpg.hide_item("Renter Login")
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)

        dpg.add_text("Main menu", tag="renterMainMenuText")

def rent_new_car():
    dpg.delete_item("Renter Control Panel")
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
        dpg.hide_item("Renter Login")
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)

        dpg.add_text("Rent new car")

def see_rented_cars():
    dpg.delete_item("Renter Control Panel")
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
        dpg.hide_item("Renter Login")
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)

        dpg.add_text("See rented cars")

def options():
    dpg.delete_item("Renter Control Panel")
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
        dpg.hide_item("Renter Login")
        with dpg.menu_bar(label="Menu Bar"):
            # dpg.add_menu_item(label="Rent a new car")
            dpg.add_button(label="Home", callback=log_in_accepted)
            dpg.add_button(label="Rent a new car", callback=rent_new_car)
            dpg.add_menu_item(label="Rented cars", callback=see_rented_cars)
            dpg.add_menu_item(label="Options", callback=options)

        dpg.add_text("Options")
