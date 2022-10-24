import dearpygui.dearpygui as dpg

def log_in_accepted():
    dpg.delete_item("Admin Control Panel")
    with dpg.window(label="Admin Control Panel", tag="Admin Control Panel", width=400, height=400):
        dpg.hide_item("Admin Login")
        dpg.add_text("TEST")