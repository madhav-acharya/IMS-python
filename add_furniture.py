from read import get_original
def add_furniture(furniture_id):
    added_li = []

    txt_items = get_original()
    id_li = []
    for i in range(len(txt_items)):
        id_li.append(txt_items[i]["id"])

    is_id_valid = False
    while is_id_valid == False:
        # try:
        #     # furniture_id = input("Enter the furniture ID: ")
        #     if int(furniture_id) <= 0:
        #         raise ValueError("Negative values are not allowed since furniture id started from 1")
        # except ValueError as e:
        #     print("Value Error, ", e)
        #     continue
        # furniture_id = furniture_id
        if furniture_id in id_li:
            print("This id already exist, please enter another id")
            is_id_valid = False
        else:
            is_id_valid = True

    null_value = True
    manufacturer = ""
    furniture_name = ""
    quantity = ""
    rate = ""

    while null_value:
        try:
            manufacturer = input("Enter the manufacturer name: ")
            if manufacturer == "" or manufacturer.isnumeric():
                raise ValueError("manufacturer name cannot be empty or numeric")
            furniture_name = input("Enter the name of Furniture item: ")
            if furniture_name == "" or furniture_name.isnumeric():
                raise ValueError("furniture name cannot be empty or numeric")
            quantity = input("Enter the quantity: ")
            if quantity.isalpha()  or quantity == "" or int(quantity) <= 0:
                raise ValueError("Negative, null or alphabetical values are not allowed ")
            rate = input("Enter the price per item: ")
            if rate.isalpha() or rate == "" or int(rate) <= 0 :
                raise ValueError("Negative, null or alphabeticals values are not allowed ")
            null_value = False
        except ValueError as error:
            null_value = True
            print(error)
            continue

    added_li.append(str(furniture_id))
    added_li.append(manufacturer)
    added_li.append(furniture_name)
    added_li.append(quantity)
    added_li.append("$"+rate)

    li_to_str = ", ".join(added_li)

    with open("furniture_data.txt", "a") as data:
        data.seek(0, 2)
        data.write("\n" +li_to_str)
        print("Data aaded sucessfully")

