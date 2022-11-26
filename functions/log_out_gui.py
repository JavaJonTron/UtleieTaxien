from functions import delete_windows
import dearpygui.dearpygui as dpg
from functions import log_off_func


# Not testable due to GUI
def log_out(human_list):
    delete_windows.delete_windows_func()
    log_off_func.log_off_human(human_list)
    dpg.set_primary_window("Main menu", True)
