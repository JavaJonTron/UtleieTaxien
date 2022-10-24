import dearpygui.dearpygui as dpg


from functions import gui_main_menu_functions as gui_func


dpg.create_context()
dpg.create_viewport(title='Utleie_app', width=600, height=600)

# with dpg.window(label="RENTER", tag="RENTER"):
    # dpg.add_text("Dette er en test tekst")

with dpg.window(label="Main menu", tag="Main menu"):
    dpg.add_text("Log in")
    dpg.add_button(label="Log in as renter", tag="renterLogin", callback=gui_func.renter_Login)
    dpg.add_button(label="Log in as owner", tag="ownerLogin", callback=gui_func.owner_Login)
    dpg.add_button(label="Log in as admin", tag="adminLogin", callback=gui_func.admin_Login)




# med render loop vil vi fjerne start_dearpygui
dpg.set_primary_window("Main menu", True)

# below replaces, start_dearpygui()
#while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
#    print("this will run every frame")
#    dpg.render_dearpygui_frame()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()