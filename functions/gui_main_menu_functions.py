import dearpygui.dearpygui as dpg
from functions import gui_admin_menu_functions as gui_admin_func
from functions import gui_owner_menu_functions as gui_owner_func
from functions import gui_renter_menu_functions as gui_renter_func
from main import owner_list
from main import renter_list

def admin_Login():
    dpg.delete_item("Admin Login")
    dpg.hide_item("Main menu")
    with dpg.window(label="Admin Login", tag="Admin Login", width=300, height=200):
        dpg.set_primary_window("Admin Login", True)
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Admin username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Admin password")
        dpg.add_button(label="Log in", tag="adminLogInButton", callback=gui_admin_func.log_in_accepted)

def owner_Login():
    dpg.delete_item("Owner Login")
    dpg.hide_item("Main menu")
    with dpg.window(label="Owner Login", tag="Owner Login", width=300, height=200):
        dpg.set_primary_window("Owner Login", True)
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Owner username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Owner password")
        dpg.add_button(label="Owner 1 Log in", tag="owner1LogInButton", callback=gui_owner_func.log_in_accepted,
                       user_data=owner_list[0])
        dpg.add_button(label="Owner 2 Log in", tag="owner2LogInButton", callback=gui_owner_func.log_in_accepted,
                       user_data=owner_list[1])
        # dpg.add_button(label="Owner Log in with Google", tag="ownerLogInGoogleButton", callback=gui_owner_func.log_in_accepted)
        # dpg.add_button(label="Owner Log in with Vipps", tag="ownerLogInVippsButton", callback=gui_owner_func.log_in_accepted)

def renter_Login():
    dpg.delete_item("Renter Login")
    dpg.hide_item("Main menu")
    with dpg.window(label="Renter Login", tag="Renter Login", width=300, height=200):
        dpg.set_primary_window("Renter Login", True)
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Renter username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Renter password")
        dpg.add_button(label="Renter 1 Log in", tag="renter1LogInButton", callback=gui_renter_func.log_in_accepted,
                       user_data=renter_list[0])
        dpg.add_button(label="Renter 2 Log in", tag="renter2LogInButton", callback=gui_renter_func.log_in_accepted,
                       user_data=renter_list[1])
        dpg.add_button(label="Renter Log in", tag="renterLogInButton")
        dpg.add_button(label="Renter Log in with Google", tag="renterLogInGoogleButton")
        dpg.add_button(label="Renter Log in with Vipps", tag="renterLogInVippsButton")






