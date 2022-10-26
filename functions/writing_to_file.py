from classes import file_handler_json as fhj

def writing(filename, information):
    handler = fhj.File_handler_json(filename, information)
    print(f"Dette skal være informasjonen vi prøver å skrive til fil{information}")
    handler.write_method()
    del(handler)
# DEN SLETTER JO BARE VARIABEL REFERAN SEN IKKE OBJEKTET