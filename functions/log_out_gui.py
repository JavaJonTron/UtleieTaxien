from functions import delete_windows
import dearpygui.dearpygui as dpg
from functions import log_off_func
from main import renter_list
#from GUI import MenuMain_gui.
def log_out(human_list):
    delete_windows.delete_windows_func()
    log_off_func.log_off_human(human_list)
    dpg.set_primary_window("Main menu", True)
    #for renter in log_off_func(renter_list):
    #   renter.is_logged_in = False
    #dpg.hide_item("Main menu", False)


