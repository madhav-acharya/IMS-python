def read_txt_file():
    """This is the function to read txt file and return it"""
    with open("furniture_data.txt", "r") as file:
        print(file.read())
        return file
    
def convert_txt_to_list():
    """This is the function which convert txt file to the list of dictionary from the txt file"""
    furniture_lists = []
    with open("furniture_data.txt", "r") as file:
        for lines in file:
            id, name_of_manufacturers, product_name, quantity, price_per_unit = lines.strip().split(", ")
            furniture_lists.append(
                {
                    "id": id,
                    "name_of_manufacturer": name_of_manufacturers,
                    "product_name": product_name,
                    "quantity": int(quantity),
                    "price_per_unit": int(price_per_unit[1:])
                }
            )
        return furniture_lists
convert_txt_to_list()

# get original datatypes values
def get_original():
    """This is the function which convert data got from txt to list of dictionary without changing its datatype"""
    furniture_lists = []
    with open("furniture_data.txt", "r") as file:
        for lines in file:
            id, name_of_manufacturers, product_name, p_quantity, price_per_unit = lines.strip().split(", ")
            furniture_lists.append(
                {
                    "id": id,
                    "name_of_manufacturer": name_of_manufacturers,
                    "product_name": product_name,
                    "quantity": p_quantity,
                    "price_per_unit": price_per_unit
                }
            )
        return furniture_lists
    
def display_furniture():
    """This is the function to display the available items which is stored in txt file"""
    items = get_original()
    fur_items = f""""""

    for length in range(len(items)):
        fur_items += f"""| {items[length]["id"]:<5} | {items[length]["name_of_manufacturer"]:<30} | {items[length]["product_name"]:<15} | {items[length]["quantity"]:<10} | {items[length]["price_per_unit"]:<5}|\n"""
    title = f"""\n| {"ID":<5} | {"Name Of Manufacturer":<30} | {"Product Name":<15} | {"Quantity":<10} | {"Price":<5}|\n\n"""
    print(title + fur_items)
