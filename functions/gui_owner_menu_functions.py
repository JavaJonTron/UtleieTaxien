import dearpygui.dearpygui as dpg
import dummyObjects.dummyOwner1 as dummy1

def log_in_accepted():
    dpg.delete_item("Owner Control Panel")
    with dpg.window(label="Owner Control Panel", tag="Owner Control Panel", width=400, height=400):
        #dpg.hide_item("Owner Login")
        dpg.add_text("TEST")
        dpg.add_button(label="Create owner", callback=dummy1.create_owner())