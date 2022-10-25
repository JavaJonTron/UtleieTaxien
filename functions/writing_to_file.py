from classes import file_handler_json as fhj

def writing(filename, information):
    handler = fhj.File_handler_json(filename, information)
    handler.write_method()