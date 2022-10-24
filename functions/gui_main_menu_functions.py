import dearpygui.dearpygui as dpg
from functions import gui_admin_menu_functions as gui_admin_func
def test():
    print("TESTER HER")

def UItest():
    print ("TESTEN FUNGERTE")

def admin_Login():
    with dpg.window(label="Admin Login", tag="Admin Login", width=300, height=200):
        dpg.add_text("Username:")
        dpg.add_input_text(tag="username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="password")
        dpg.add_button(label="Log in", tag="adminLogInButton", callback=gui_admin_func.log_in_accepted)

