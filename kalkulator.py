import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def add(a, b):
    logging.info(f"Dodaję {a} i {b}.")
    return a + b

def sub(a, b):
    logging.info(f"Odejmuję {a} i {b}.")
    return a - b

def multi(a, b):
    logging.info("Mnożę %s i %s." % (str(a), str(b)))
    return a * b

def div(a, b):
    logging.info("Dzielę %s i %s." % (str(a), str(b)))
    return a / b
    
def get_data():
    op = input("Podaj działanie, posługując się odpowiednią liczbą: 1 - Dodawanie, 2 - Odejmowanie, 3 - Mnożenie, 4 - Dzielenie: ")
    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))     
    return op, a, b

operations = {
    "1": add,
    "2": sub,
    "3": multi,
    "4": div,
}

def main():
    op, a, b = get_data()
    try:
        result = operations[op](a, b)
        print("Wynik to: ", result)
    except KeyError:
        print("Nieznana operacja!")
    
    #result = operations.get(op, lambda x, y: print("Nieznana operacja"))(a, b)


if __name__ == "__main__":
    # print(add)
    # print(add(1, 2))
    # # main().
    # print(operations["1"])
    # print(operations["1"](1, 2))

    main()