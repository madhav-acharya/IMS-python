from read import get_original
# update txt after buying furniture
def update_txt_purchase(product_id, quantity):
    """This is the function to update the txt after buying """
    
    li_of_di = get_original()
    updated_items = []
    updated_txt = """"""

    for i in range(len(li_of_di)):
        if int(li_of_di[i]["id"]) == int(product_id):
            li_of_di[i]["quantity"] = int(quantity) + int(li_of_di[i]["quantity"])
            q = str(li_of_di[i]["quantity"])
            li_of_di[i]["quantity"] = str(q)
            updated_items = li_of_di
            break
    for i in range(len(updated_items)):
        updated_txt += ", ".join(updated_items[i].values()) + "\n"
    
    with open("furniture_data.txt", "w") as updated_file:
        updated_file.write(updated_txt)
    

# update txt after selling furniture
def update_txt_sell(product_id, quantity):
    """This is the function to update txt after selling"""

    li_of_di = get_original()
    updated_items = []
    updated_txt = """"""

    for i in range(len(li_of_di)):
        if int(li_of_di[i]["id"]) == int(product_id):
            li_of_di[i]["quantity"] =  int(li_of_di[i]["quantity"]) - int(quantity)
            q = str(li_of_di[i]["quantity"])
            li_of_di[i]["quantity"] = str(q)
            updated_items = li_of_di
            break
    for i in range(len(updated_items)):
        updated_txt += ", ".join(updated_items[i].values()) + "\n"
    
    with open("furniture_data.txt", "w") as updated_file:
        updated_file.write(updated_txt)