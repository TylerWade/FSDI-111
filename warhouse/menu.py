import datetime


def print_menu():
    print("\n\n")
    print("*" * 40)
    print("  Warehouse Control System" + "\n  " + get_date_time())
    print("*" * 40)

    print("[1] Register New Item")
    print("[2] List All Items")
    print("[3] Update Stock")
    print("[4] List items and Stock")
    print("[5] Remove Item from the system")
    print("[6] Log an Event")  # the warehouse purchased some stuff
    print("[7] View Event Log")  # you sold something
    print("[8] List total stock inventory")

    print("[x] Exit the System")


def get_date_time():
    current = datetime.datetime.now()
    time = current.strftime("%c")
    return time
