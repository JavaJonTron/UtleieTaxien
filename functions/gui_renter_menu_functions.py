import dearpygui.dearpygui as dpg

def log_in_accepted():
    with dpg.window(label="Renter Control Panel", tag="Renter Control Panel", width=400, height=400):
        dpg.hide_item("Renter Login")
        dpg.add_text("TEST")