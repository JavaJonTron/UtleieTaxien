from admin.admin import Admin

def create_admin():
    name = "Admin"
    is_logged_in = False
    return Admin(name, is_logged_in)

