import sys
import logging

logging.basicConfig(level=logging.INFO)

def operation(number_1, number_2):
    if operation_type == '1':
        logging.info(f"Dodaję {number_1} i {number_2}")
        result = number_1 + number_2

    elif operation_type == '2':
        logging.info(f"Odejmuję {number_1} i {number_2}")
        result = number_1 - number_2

    elif operation_type == '3':
        logging.info(f"Mnożę {number_1} i {number_2}")
        result = number_1 * number_2

    elif operation_type == '4':
        logging.info(f"Dzielę {number_1} i {number_2}")
        result = number_1 / number_2
    return result

if __name__ == "__main__":
    operation_type = (input("Podaj działanie, posługując się odpowiednią liczbą:\n"+"1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: "))
    number_1 = int(input("Podaj składnik 1: "))
    number_2 = int(input("Podaj składnik 2: "))


    res = operation(number_1, number_2)
    print(res)


    

