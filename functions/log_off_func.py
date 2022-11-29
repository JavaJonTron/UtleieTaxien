def log_off_human(human_list):
    """
    Logger av objekter som har arvet fra Human klassen
    :param human_list: Liste med Human objekter
    :return:
    """
    for human_obj in human_list:
        human_obj.is_logged_in = False
