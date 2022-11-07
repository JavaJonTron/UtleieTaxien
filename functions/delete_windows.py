import dearpygui.dearpygui as dpg
renter_window_list = ["Renter Main", "Renter New Car", "Renter Car", "Renter See Cars", "Renter Options"]


def delete_windows_func():
    for window in renter_window_list:
        dpg.delete_item(window)
