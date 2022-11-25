def checking_object_instance(object_type, class_type):
    '''
    Sjekker om et object er av en type klasse.
    :param object_type: Bruker som er innolgget
    :param class_type: Klassen som er i bruk
    :return: True eller False om et object er en klasse
    '''
    if isinstance(object_type, class_type):
        return True
    else:
        return False
