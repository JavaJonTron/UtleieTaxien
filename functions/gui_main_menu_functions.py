import dearpygui.dearpygui as dpg
def test():
    print("TESTER HER")

def UItest():
    print ("TESTEN FUNGERTE")

def admin_Login():
    with dpg.window(label="Admin Login", tag="Admin Login", width=300, height=200):
        dpg.add_text("Username:")
        dpg.add_input_text(Label="Username", tag="username")
        dpg.add_text("Password:")
        dpg.add_input_text(Label="Password", tag="password")
