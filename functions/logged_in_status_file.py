from main import renter_list


def logged_in_status():
    for renter_obj in renter_list:
        if renter_obj.is_logged_in:
            print(renter_obj.is_logged_in)
            return renter_obj
