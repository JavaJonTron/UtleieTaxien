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
    # score_list = [5, 10, 100]
    # score = round(functions.get_average_of_list.average_list(score_list))
    score = 10
    return Renter(age, sex, name, score)  #score_list

