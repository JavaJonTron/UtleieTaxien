from FileHandling import filehandlerpickle
from dummyObjects import dummyOwner1, dummyOwner2, dummyCar2, dummyCar3, dummyCar1, dummyRenter1, dummyRenter2, \
    dummyAdmin1

owner_list = []
car_list = []
renter_list = []
bookings_list = []
admin_list = []
# Her har vi lister som skal holde på alle objektene som blir opprettet gjennom programmet.



def dummy_car_creation(owners):
    """
    Her har vi en funksjon for å opprette dummy biler
    :param owners: Dette er en parameter for listen over eiere
    :return:
    """
    car = dummyCar1.create_car(owners[0])
    car_list.append(car)
    car = dummyCar2.create_car(owners[0])
    car_list.append(car)
    car = dummyCar3.create_car(owners[1])
    car_list.append(car)


def dummy_admin_creation():
    """
    Her har vi en funksjon for å opprette dummy admin
    :return:
    """
    admin = dummyAdmin1.create_admin()
    admin_list.append(admin)


def dummy_owner_creation():
    """
    Her har vi en funksjon for å opprette dummy utleieier objekter
    :return:
    """
    dummyOwnerList = []
    dummyOwnerList.append(dummyOwner1)
    dummyOwnerList.append(dummyOwner2)
    for dummy in dummyOwnerList:
        print(dummy)
        owner = dummy.create_owner()
        owner_list.append(owner)



def dummy_renter_creation():
    """
    Her har vi en funksjon for å opprette dummy Leie objekter
    :return:
    """
    dummyRenterList = []
    dummyRenterList.append(dummyRenter1)
    dummyRenterList.append(dummyRenter2)
    for dummy in dummyRenterList:
        renter = dummy.create_renter()
        renter_list.append(renter)

def save_system(file, current_list):
    """
    Dette er en funksjon som brukes til å lagre listene over på sin egen fil.
    Et file handler objekt blir opprettet og man kaller på den innebygde skrivemetoden.
    :param file: Dette er filen man skal lagre til
    :param current_list: Dette er hvilken liste man skal lagre
    :return:
    """
    filskriving = filehandlerpickle.FileHandlerPickle(file, current_list)
    filskriving.write_method()
    del filskriving


def load_system(file, current_list):
    """
    Dette er en funksjon som brukes for å laste opp objekter fra fil til egen liste som holder på objektet
    :param file: Dette er navnet på filen man skal lese fra
    :param current_list: Dette er hvilken liste man skal laste opp filinholdet til
    :return:
    """

    filskriving = filehandlerpickle.FileHandlerPickle(file, None)
    list_from_file = filskriving.read_method()
    if list_from_file is None and filskriving.filename == 'owner_file':
        dummy_owner_creation()
    elif list_from_file is None and filskriving.filename == 'renter_file':
        dummy_renter_creation()
    elif list_from_file is None and filskriving.filename == 'car_file':
        dummy_car_creation(owner_list)
    elif list_from_file is None and filskriving.filename == 'admin_file':
        dummy_admin_creation()
    elif list_from_file is not None:
        for obj in list_from_file:
            current_list.append(obj)
        del filskriving








load_system('owner_file', owner_list)
load_system('renter_file', renter_list)
load_system('car_file', car_list)
load_system('booking_file', bookings_list)
load_system('admin_file', admin_list)





save_system('admin_file', admin_list)
save_system('owner_file', owner_list)
save_system('renter_file', renter_list)
save_system('car_file', car_list)
save_system('booking_file', bookings_list)
