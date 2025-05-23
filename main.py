from read import display_furniture
from buy_sell import buy, sell
from add_furniture import add_furniture

def menu_option():
    print("""
Welcome to the BRJ furniture store.
1) See available furniture items
2) Buy furniture
3) Sell furniture
4) Add Furniture
5) Exit
          """)
    choice = int(input("Enter your selection: "))
    return choice

def choice_selection():
    """This is the main method which is executed at first when the program is executed"""
    while True:
        try:
            choices = menu_option()
            if choices == 1:
                print("reading the file")
                display_furniture()
            elif choices == 2:
                print("you are buying")
                buy()
            elif choices == 3:
                print("you are selling")
                sell()
            elif choices == 4:
                print("You are adding furniture")
                furniture_id = int(input("Enter furniture ID: "))
                add_furniture(furniture_id)
            elif choices == 5:
                print("You have exited")
                break
            else:
                print("invalid selection")
        except ValueError as e:
            print("value error")

choice_selection()

