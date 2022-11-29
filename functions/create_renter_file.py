from renter.renter import Renter


def create_renter():
    """
    Oppretter objekter av leier utifra input, dette er ikke i bruk i programmet per nå.
    :return: Leier objekt
    :return:
    """
    name = input("Name: ").upper()
    sex = input("Sex: ").upper()
    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print("Please enter your age!")
            continue
    score = 10
    return Renter(age, sex, name, score)

