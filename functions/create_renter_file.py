from classes.renter import Renter
import functions.get_average_of_list

def create_renter():
    name = input("Name: ").upper()
    sex = input("Sex: ").upper()
    while True:
        try:
            age = int(input("Age: "))
            break
        except ValueError:
            print("Please enter your age!")
            continue
    rented = []
    score_list = [5, 10, 100]
    score = round(functions.get_average_of_list.average_list(score_list))
    return Renter(name, sex, age, rented, score, score_list)
