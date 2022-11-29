from owner.owner import Owner


def create_owner():
    """
    Oppretter objekter av eier utifra input, dette er ikke i bruk i programmet per nå.
    :return: Bil objekt
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
    owned_cars = []
    return Owner(age, sex, name, score, owned_cars, is_logged_in=False)

