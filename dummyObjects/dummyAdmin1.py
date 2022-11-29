from admin.admin import Admin

def create_admin():
    """
    Oppretter et dummy Admin objekt.
    :return: Admin objektet
    """
    name = "Admin"
    is_logged_in = False
    return Admin(name, is_logged_in)

