import dearpygui.dearpygui as dpg
from functions import gui_admin_menu_functions as gui_admin_func
from functions import gui_owner_menu_functions as gui_owner_func
from functions import gui_renter_menu_functions as gui_renter_func

def test():
    print("TESTER HER")
    dpg.show_item("RENTER")

def UItest():
    dpg.hide_item("RENTER")
    print ("TESTEN FUNGERTE")

#Begynnelse på et forsøk for å se om det er mulig å samle felles kodelogikk i en funksjon
#Eller kansje vi burde bruke en klasse?
#Det er mye kode som går igjen flere ganger med GUi og det kan kansje bli litt rotete, uryddig eller uoversiktlig?

#def login(tekst_login, width, height):
#    dpg.delete_item(tekst_login)
#    with dpg.window(label=tekst_login, tag=tekst_login, width=width, height=height):
#        dpg.add_button(label="Log in", tag="adminLogInButton", callback=gui_admin_func.log_in_accepted)
#    pass
#objectnavn.dpg.add
#login()

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
        dpg.add_button(label="Owner 1 Log in", tag="owner1LogInButton", callback=gui_owner_func.log_in_accepted, user_data=0)
        dpg.add_button(label="Owner 2 Log in", tag="owner2LogInButton", callback=gui_owner_func.log_in_accepted, user_data=1)
        # dpg.add_button(label="Owner Log in with Google", tag="ownerLogInGoogleButton", callback=gui_owner_func.log_in_accepted)
        # dpg.add_button(label="Owner Log in with Vipps", tag="ownerLogInVippsButton", callback=gui_owner_func.log_in_accepted)

def renter_Login():
    dpg.delete_item("Renter Login")
    with dpg.window(label="Renter Login", tag="Renter Login", width=300, height=200):
        dpg.add_text("Username:")
        dpg.add_input_text(tag="Renter username")
        dpg.add_text("Password:")
        dpg.add_input_text(tag="Renter password")
        #Er det egentlig nødvendig å opprette brukere via input for at programmet skal fungere?
        #Kan det heller være en bonus?
        #Sikre at kjernefunksjonaliteten til programmet fungerer først
        # også implementere brukeropprettelse hvis vi finner det nødvendig
        dpg.add_button(label="Renter Log in", tag="renterLogInButton", callback=gui_renter_func.log_in_accepted)
        dpg.add_button(label="Renter Log in with Google", tag="renterLogInGoogleButton", callback=gui_renter_func.log_in_accepted)
        dpg.add_button(label="Renter Log in with Vipps", tag="renterLogInVippsButton", callback=gui_renter_func.log_in_accepted)

