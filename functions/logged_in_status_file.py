from main import renter_list


def logged_in_status(list):
    for human_obj in list:
        if human_obj.is_logged_in:
            return human_obj
