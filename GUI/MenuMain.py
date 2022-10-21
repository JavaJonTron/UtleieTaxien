import dearpygui.dearpygui as dpg

dpg.create_context()



with dpg.window(label="Main menu", tag="Main menu"):
    dpg.add_text("Log in")
    dpg.add_button(label="Log in as renter")
    dpg.add_button(label="Log in as owner")

dpg.create_viewport(title='Utleie_app', width=600, height=200)
dpg.setup_dearpygui()
dpg.show_viewport()

#med render loop vil vi fjerne start_dearpygui
dpg.set_primary_window("Main menu", True)
dpg.start_dearpygui()
# below replaces, start_dearpygui()
#while dpg.is_dearpygui_running():
    # insert here any code you would like to run in the render loop
    # you can manually stop by using stop_dearpygui()
#    print("this will run every frame")
#    dpg.render_dearpygui_frame()
dpg.destroy_context()