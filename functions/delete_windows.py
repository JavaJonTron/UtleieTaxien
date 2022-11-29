import dearpygui.dearpygui as dpg

renter_window_list = ["Renter Login Accepted", "Renter Login", "Renter Main", "Renter New Car", "Renter Car",
                      "Renter See Cars", "Renter Options"]
owner_window_list = ["Owner Login Accepted", "Owner Login", "Owner Main", "Owner See Cars", "Owner Options",
                     "Owner New Car", "Approve Or Deny", "Approve Car", "Owner See Detailed Cars"]
admin_window_list = ["Admin Login Accepted", "Admin Login", "Admin Main", "All Cars", "Admin See Detailed Cars",
                     "Admin See Detailed Users", "All Users"]


def delete_windows_func():
    """
    Ikke testbart grunnet GUI
    Sletter tidligere vinduer når man klikker på en knapp som åpner et nytt vindu
    :return:
    """
    for window in admin_window_list:
        dpg.delete_item(window)

    for window in owner_window_list:
        dpg.delete_item(window)

    for window in renter_window_list:
        dpg.delete_item(window)
