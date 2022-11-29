def get_user_logged_in_status(human_list):
    """
    Henter informasjon om hvilke brukere som er innlogget
    :param human_list: Liste med human objekter
    :return: Human objekt som er innlogget
    """
    for human_obj in human_list:
        if human_obj.is_logged_in:
            return human_obj
