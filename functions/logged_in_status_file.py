def get_user_logged_in_status(human_list):
    for human_obj in human_list:
        if human_obj.is_logged_in:
            return human_obj
