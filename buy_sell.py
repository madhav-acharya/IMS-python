from read import convert_txt_to_list
from invoice import gen_purchase_invoice, gen_sell_invoice
from update_txt import update_txt_purchase, update_txt_sell
from add_furniture import add_furniture

# finds index from product id
def index_finder(product_id, li_of_di):
    """This is the function which takes id and list of dictionary got from the txt file after reading to find the index of the items from the ID"""
    index = 0
    for indexes in range(len(li_of_di)):
        if int(product_id) == int(li_of_di[indexes]["id"]):
            index = indexes
            return index

# function to buy products
def buy():
    """This is the function which ask input needed for buying and helps in buying furniture"""
    li_of_di = convert_txt_to_list()
    id_in_li = []
    for i in range(len(li_of_di)):
        id_in_li.append(li_of_di[i]["id"])
        
    null_value = True
    emp_name = ""
    ph_no = ""
    location = ""
    while null_value:
        try:
            emp_name = input("Enter your name: ")
            if emp_name == "" or not emp_name.replace(" ", "").isalpha():
                raise ValueError("name cannot be empty or in numbers")
            location = input("Enter your location: ")
            if location == "" or not location.replace(" ", "").isalnum():
                raise ValueError("location cannot be empty")
            ph_no = input("Enter your phone no: ")
            if ph_no == "" or not ph_no.isnumeric():
                raise ValueError("phone number cannot be empty or in alphabet")
            null_value = False
        except ValueError as error:
            null_value = True
            print(error)
            continue
    continue_purchase = True
    product_id_li = []
    quantity_li = []
    index_li = []
    manufacturer_li = []
    product_name_li = []
    price_per_unit_li = []
    total_amount_li = []

    while continue_purchase:
        try:
            product_id = int(input("Enter the product ID: "))
            if product_id <= 0 :
                raise ValueError("Negative values are not allowed since product id started from 1")
            want_to_add = ""
            if str(product_id) not in id_in_li:
                print("The product with this ID is not available")
                print("Do you want to add product with this ID?")
                want_to_add = input("Enter 'yes' to add 'no' to skip: ")
            if want_to_add.lower() == "yes":
                add_furniture(product_id)
            elif want_to_add.lower() == "no":
                return
            quantity = int(input("Enter the required quantity: "))
            if quantity <= 0 or str(quantity).isalpha():
                raise ValueError("Negative values are not allowed since quantity cant be less than zero or in alphabet")
        except ValueError as e:
            print("value error, ",e)
            continue

        li_of_di = convert_txt_to_list()
        index = index_finder(product_id, li_of_di)
        manufacturer = li_of_di[index]["name_of_manufacturer"]
        product_name = li_of_di[index]["product_name"]
        price_per_unit = li_of_di[index]["price_per_unit"]
        total_amount = price_per_unit * quantity

        product_id_li.append(product_id)
        quantity_li.append(quantity)
        index_li.append(index)
        manufacturer_li.append(manufacturer)
        product_name_li.append(product_name)
        price_per_unit_li.append(price_per_unit)
        total_amount_li.append(total_amount)

        # passing the parameter to the function to update the txt after buying products
        update_txt_purchase(product_id, quantity)

        # condition to ask wheather to exit or buy more
        print("want to buy more? Type 'yes' to continue or 'no' to exit and generate receipt")
        decesion = input("Enter your decesion: ")
        if decesion.lower() == "yes":
            print("You have continued")
            continue_purchase = True
        elif decesion.lower() == "no":
            print("you have exited and the invoice has been generated")
            continue_purchase = False
        else:
            print("Invalid selection")
    
    # passing the parameters to the function to generate invoice
    gen_purchase_invoice(product_id_li, manufacturer_li, product_name_li, quantity_li, price_per_unit_li, emp_name, total_amount_li, location, ph_no)
    return

# function to sell products
def sell():
    """This is a function which ask the inputs required for selling furniture"""
    li_of_di = convert_txt_to_list()
    id_in_li = []
    for i in range(len(li_of_di)):
        id_in_li.append(li_of_di[i]["id"])
    null_value = True
    cus_name = ""
    ph_no = ""
    location = ""
    while null_value:
        try:
            cus_name = input("Enter your name: ")
            if cus_name == "" or not cus_name.replace(" ", "").isalpha():
                raise ValueError("name cannot be empty or in numbers")
            location = input("Enter your location: ")
            if location == "" or not location.replace(" ", "").isalnum():
                raise ValueError("location cannot be empty")
            ph_no = input("Enter your phone no: ")
            if ph_no == "" or not ph_no.isnumeric():
                raise ValueError("phone number cannot be empty or alphabetical")
            null_value = False
        except ValueError as error:
            null_value = True
            print(error)
            continue

    continue_sell = True
    product_id_li = []
    quantity_li = []
    index_li = []
    manufacturer_li = []
    product_name_li = []
    price_per_unit_li = []
    total_amount_li = []
    vat_li = []
    
    while continue_sell:
        try:
            product_id = int(input("Enter the product ID: "))
            if product_id <= 0:
                raise ValueError("Negative values are not allowed since product id started from 1")
            want_to_add = ""
            if str(product_id) not in id_in_li:
                print("The product with this ID is not available")
                print("Do you want to add product with this ID?")
                want_to_add = input("Enter 'yes' to add 'no' to skip: ")
            if want_to_add.lower() == "yes":
                add_furniture(product_id)
            elif want_to_add.lower() == "no":
                return
        except ValueError as e:
            print("Value error, ", e)
            continue
        
        li_of_di = convert_txt_to_list()
        index = index_finder(product_id, li_of_di)
        try:
            quantity = int(input("Enter the required quantity: "))
            if quantity <= 0 or not str(quantity).isnumeric():
                raise ValueError("Negative values are not allowed since quantity cant be less than 1 or alphabetical")
        except ValueError as e:
            print("Value error, ", e)
            continue
        total_amount = 0
        shipping_cost = 0
        vat = 0
        # condition which check wheather the products are enough if product are not enough then it gives messages else it will continue
        if quantity > li_of_di[index]["quantity"]:
            print("Sorry, we donot have that much stock. we have only ", li_of_di[index]["quantity"])
        else:
            manufacturer = li_of_di[index]["name_of_manufacturer"]
            product_name = li_of_di[index]["product_name"]
            price_per_unit = li_of_di[index]["price_per_unit"]
            total_amount = int(price_per_unit * quantity) 
            vat = int(total_amount * 0.13)

            product_id_li.append(product_id)
            quantity_li.append(quantity)
            index_li.append(index)
            manufacturer_li.append(manufacturer)
            product_name_li.append(product_name)
            price_per_unit_li.append(price_per_unit)
            total_amount_li.append(total_amount)
            vat_li.append(vat)

            # passing the parameter to the function to update the txt after selling products
            update_txt_sell(product_id, quantity)

            # condition to ask wheather to exit or sell more
            print("want to sell more? Type 'yes' to continue or 'no' to exit and generate receipt")
            decesion = input("Enter your decesion: ")
            if decesion.lower() == "yes":
                print("You have continued")
                continue_sell = True
            elif decesion.lower() == "no":
                try:
                    shipping_cost = int(input("Enter shipping cost: "))
                    if shipping_cost <= 0 or not str(shipping_cost).isnumeric():
                        raise ValueError("Negative values are not allowed since shipping cost cant be less than 1 or alphabetical")
                except ValueError as e:
                    print("Value error, ", e)
                    continue
                print("you have exited and the invoice has been generated")
                continue_sell = False
            else:
                print("invalid option")
                return
    
        # passing the parameters to the function to generate invoice
    gen_sell_invoice(product_id_li, manufacturer_li, product_name_li, quantity_li, price_per_unit_li, cus_name, location, ph_no, shipping_cost,vat_li, total_amount_li)
    return 