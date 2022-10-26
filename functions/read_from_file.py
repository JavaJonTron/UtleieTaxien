from classes import file_handler_json as fhj

def reading(filename):
    handler = fhj.File_handler_json(filename)
    print(f"Dette skal være informasjonen vi prøver å lese fra fil")
    read = handler.read_method()
    print(read)
    del(handler)
#DEN SLETTER JO BARE VARIABEL REFERAN SEN IKKE OBJEKTET