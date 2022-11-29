from functions import delete_windows
import dearpygui.dearpygui as dpg
from functions import log_off_func


def log_out(human_list):
    """
    Ikke testbar grunnet GUI
    Håndterer alt som skal gjøres når noen logges av, kaller på slet vinduer funksjon, kaller på log_off_func
    :param human_list: Liste med Human objekter
    :return:
    """
    delete_windows.delete_windows_func()
    log_off_func.log_off_human(human_list)
    dpg.set_primary_window("Main menu", True)
