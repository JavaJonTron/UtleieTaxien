from owner.owner import Owner


def create_owner():
    name = input("Name: ").upper()
    sex = input("Sex: ").upper()
    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print("Please enter your age!")
            continue
    # score_list = [5, 10, 100]
    # score = round(functions.get_average_of_list.average_list(score_list))
    score = 10
    owned_cars = []
    return Owner(age, sex, name, score, owned_cars, is_logged_in=False)  # score_list

