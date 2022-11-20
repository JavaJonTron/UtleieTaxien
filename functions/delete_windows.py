import dearpygui.dearpygui as dpg

renter_window_list = ["Renter Login Accepted", "Renter Login", "Renter Main", "Renter New Car", "Renter Car",
                      "Renter See Cars", "Renter Options"]
owner_window_list = ["Owner Login Accepted", "Owner Login", "Owner Main", "Owner See Cars", "Owner Options",
                     "Owner New Car", "Approve Or Deny"]
admin_window_list = []


def delete_windows_func():
    for window in admin_window_list:
        dpg.delete_item(window)

    for window in owner_window_list:
        dpg.delete_item(window)

    for window in renter_window_list:
        dpg.delete_item(window)
