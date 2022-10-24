import dearpygui.dearpygui as dpg
from functions import gui_admin_menu_functions as gui_admin_func
from functions import gui_owner_menu_functions as gui_owner_func
from functions import gui_renter_menu_functions as gui_renter_func

def test():
    print("TESTER HER")
    dpg.show_item("RENTER")

def UItest():
    dpg.hide_item("RENTER")
    #hide_item("item")
    print ("TESTEN FUNGERTE")

def admin_Login():
    dpg.delete_item("Admin Login")
    with dpg.window(label="Admin Login", tag="Admin Login", width=300, height=200):
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Admin username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Admin password")
        dpg.add_button(label="Log in", tag="adminLogInButton", callback=gui_admin_func.log_in_accepted)

def owner_Login():
    dpg.delete_item("Owner Login")
    with dpg.window(label="Owner Login", tag="Owner Login", width=300, height=200):
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Owner username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Owner password")
        dpg.add_button(label="Owner Log in", tag="ownerLogInButton", callback=gui_owner_func.log_in_accepted)
        dpg.add_button(label="Owner Log in with Google", tag="ownerLogInGoogleButton", callback=gui_owner_func.log_in_accepted)
        dpg.add_button(label="Owner Log in with Vipps", tag="ownerLogInVippsButton", callback=gui_owner_func.log_in_accepted)

def renter_Login():
    dpg.delete_item("Renter Login")
    with dpg.window(label="Renter Login", tag="Renter Login", width=300, height=200):
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Renter username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Renter password")
        dpg.add_button(label="Renter Log in", tag="renterLogInButton", callback=gui_renter_func.log_in_accepted)
        dpg.add_button(label="Renter Log in with Google", tag="renterLogInGoogleButton", callback=gui_renter_func.log_in_accepted)
        dpg.add_button(label="Renter Log in with Vipps", tag="renterLogInVippsButton", callback=gui_renter_func.log_in_accepted)

