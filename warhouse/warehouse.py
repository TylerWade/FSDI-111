

"""
Program: Warehouse control system
Functionality:
    1- register new items on the system
        * id(auto generate this)
        * title
        * category
        * price
        * stock(how many in warehouse)

    2- list the items on the system
    3- update quantity on stock for selected item
    4- list items_list with stock (stock > 0)

    5- Remove
    6- Entry
    7- Output
    8- See event log
    9- See stock value
"""
import sys
from menu import print_menu
from item import Item
import pickle
import os


def clear(): return os.system('cls')


items_list = []  # array to store the data
event_log = []
id_count = 1
items_file = "items.data"
log_file = "log.data"

# def the register item function
# ask for the info
# create a new object
# store the object on an array
# item = Item(id, title,...)


def save_items():
    try:
        writer = open(items_file, "wb")  # wb = write binary information
        pickle.dump(items_list, writer)
        writer.close()
        print("item Saved!!")
    except:
        print(" **Error: Data could not be saved!!")


def read_items():
    global id_count
    global items_file

    try:
        reader = open(items_file, "rb")
        temp_data = pickle.load(reader)

        for item in temp_data:
            items_list.append(item)

        last = items_list[-1]
        id_count = last.Iid + 1

        print("Data Loaded: " + str(len(items_list)) + " items")
    except:
        print(" **Error: Data could not the loaded!")


def remove_item():
    item = select_item()
    if(item is not None):
        items_list.remove(item)
        print("Item Removed!!")


"""
Stock value:
- travel the items array
- get the total(value) for each item (stock * price)
- sum the totals of each item
- Display the result
"""


def list_all_stock():
    print("\n\n")
    print("*" * 40)
    print("  List All items Stock Value")
    print("*" * 40)

    all_stock = 0
    for item in items_list:
        stock_value = item.price * item.stock
        all_stock += stock_value

        if(item.stock <= 0):
            print("ID: " + str(item.Iid) +
                  "\n" "Title: " + item.title +
                  "\n" "*****OUT OF STOCK..." +
                  "\n" "Shelf Number: ",  id(item),
                  "\n"+"*" * 40)
        else:

            print("ID: " + str(item.Iid) +
                  "\n" "Title: " + item.title +
                  "\n" "Price: $" + str(item.price) +
                  "\n" "In Stock: " + str(item.stock) +
                  "\n" "Stock Value: $" + str(stock_value) +
                  "\n" "Shelf Number: ",  id(item),
                  "\n" + "*" * 40)
        print("*" * 40)
        print("\n")
    print("All Stock Value: $" + str(all_stock)+"\n"+"*"*40)


def log_entry():
    print("\n\n")
    print("*" * 40)
    print("  Create Event Log")
    print("*" * 40)
    # for item in items_list:
    item = select_item()
    if(item is not None):
        how_many_in = int(input("How many added to stock: "))
        how_many_out = int(input("How many sold: "))

        item.stock = item.stock + how_many_in - how_many_out

        event = '| ID:' + str(item.Iid) + " | " + item.title + " | Added to stock: " + str(
            how_many_in) + " | Sold: " + str(how_many_out) + " | Updated stock: " + str(item.stock)

        event_log.append(event)
    print("*" * 50)
    print("\n"+event+"\n")


def save_log():
    try:
        writer = open(log_file, "wb")  # wb = write binary information
        pickle.dump(event_log, writer)
        writer.close()
        print("Log Saved!!")
    except:
        print(" **Error: Log could not be saved!!")


def print_log():
    print("\n\n")
    print("*" * 40)
    print("  List of All Logged events")
    print("*" * 40)
    for i in range(len(event_log)):
        print(i, end=" ")
        print(event_log[i])


def read_log():
    global log_file
    global event_log

    try:
        reader = open(log_file, "rb")
        log_data = pickle.load(reader)

        for log in log_data:
            event_log.append(log)

        print("Data Loaded: " + str(len(event_log)) + " items")
    except:
        print(" **Error: Data could not the loaded!")


def register_item():
    global id_count
    print("\n\n")
    print("*" * 40)
    print("  Register New Item")
    print("*" * 40)

    try:
        title = input("Title of Item: ")
        price = float(input("Price of Item: "))
        category = input("Category of Item: ")
        stock = int(input("How many items in Stock: "))
        Iid = id_count

        new_item = Item(id, title, category, price, stock, Iid)
        items_list.append(new_item)
        id_count += 1
        print("Item Created")

    except:
        print("Error, verify and try again!")
        print("**Error: ", sys.exc_info()[0])


def list_all():
    print("\n")
    print("*" * 40)
    print("  List All items")
    print("*" * 40)

    for item in items_list:
        if(item.stock <= 0):
            print("ID: " + str(item.Iid) +
                  "\n" "Title: " + item.title +
                  "\n" "Shelf Number: ",  id(item),
                  "\n" "OUT OF STOCK..." + str(item.stock))
        else:
            print("ID: " + str(item.Iid) +
                  "\n" "Title: " + item.title +
                  "\n" "Price: $" + str(item.price) +
                  "\n" "Category: " + item.category +
                  "\n" "In Stock: " + str(item.stock) +
                  "\n" "Shelf Number: ", id(item))
        print("*" * 40)
        print("\n")


def update_stock():
    item = select_item()
    if(item is not None):
        try:
            # ask for new stock value
            new_stock = int(input("New Stock Value: "))
            # assign the stock to item
            item.stock = new_stock
        except:
            print("Error, update")


def select_item():
    print("\n")
    list_all()
    # search the item with ID equal to selection
    # return the matching element
    # retrun none if not found
    selection = int(input("ID of Item: "))
    for item in items_list:
        if(item.Iid == selection):
            print("Title: " + item.title +
                  "\n" "Price: " + str(item.price) +
                  "\n" "Category: " + item.category +
                  "\n" "In Stock: " + str(item.stock) +
                  "\n" "Shelf Number: ", id(item))
            return item


def list_item_stock():
    print("\n\n")
    print("*" * 40)
    print("  List All items with stock")
    print("*" * 40)
    for item in items_list:
        if(item.stock > 0):
            print("Title: " + item.title + "---In Stock: " + str(item.stock))


# First thing is to read previous data
print("\n\n\n")
print("*" * 40)
print("  DataBase Information")
print("*" * 40)
read_items()
read_log()


# go onto the menu
opc = ""
while (opc != 'x'):
    clear()
    print_menu()
    opc = input("Select and option: ")
    clear()

    if(opc == '1'):
        register_item()
        save_items()

    elif(opc == '2'):
        list_all()

    elif(opc == '3'):
        update_stock()
        save_items()

    elif(opc == '4'):
        list_item_stock()

    elif(opc == '5'):
        remove_item()
        save_items()

    elif(opc == '6'):
        log_entry()
        save_items()
        save_log()

    elif(opc == '7'):
        print_log()

    elif(opc == '8'):
        list_all_stock()

    if(opc != 'x'):
        input("\n\nPress Enter to Continue...")

print("Exiting System... ")
