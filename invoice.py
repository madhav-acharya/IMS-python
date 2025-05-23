import datetime

# function to generate the invoice taking the parameters
def gen_purchase_invoice(id, manufacturer, product_name, quantity, price_per_unit, emp_name, total_amount, location, ph_no):
    """This is the function to generate invoice after purchasing furniture"""
    print("purchase invoive has been generated")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")
    date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    receipt_name = f"""{emp_name.lower().replace(" ", "")}purchase-receipt{date_time}.txt"""

    uni_purchase_details = f"""
    {"--------------------------------------------Purchase receipt-------------------------------------------":^110}
     
    {"BRJ Furniture Store":<60} {"Date of purchase: "}{date} 
    {"SundarHaraincha-07,Gothgaun,Morang":<60} Time of purchase: {time} 
    {"PHONE- +977-9819394472 ":<60} Name of employee(Purchaser): {emp_name}  
    {"ESTD.- 2059 BS":<60} Location: {location}
    Invoice num: {datetime.datetime.now().strftime("%H%M%S"):<47} Phone No: {ph_no}                                              

    |{"SN":^3} | {"ID":^3} | {"Furniture Name":^15} | {"Manufacturer":^30} | {"Quantity":^10} | {"Price/unit":^12} | {"Total":^10}|     
    """
    multi_purchase_details = f""""""
    multi_purchase_total = 0
    for purchase_count in range(len(id)):
        multi_purchase_total += total_amount[purchase_count]
        multi_purchase_details += f"""
    |{purchase_count+1:<3} | {id[purchase_count]:<3} | {product_name[purchase_count]:<15} | {manufacturer[purchase_count]:<30} | {quantity[purchase_count]:<10} | ${price_per_unit[purchase_count]:<11} | ${total_amount[purchase_count]:<9}|
        """

    final_purchase_details = f"""{uni_purchase_details} {multi_purchase_details} 
    {"|":>76} {"Grand total:":<11} | {"$":>1}{multi_purchase_total:<9}|"""
    print(final_purchase_details)

    with open(receipt_name, "w") as receipt:
        receipt.write(final_purchase_details)

# function to generate invoice taking the parameters
def gen_sell_invoice(product_id, manufacturer, product_name, quantity, price_per_unit, cus_name, location, ph_no, shipping_cost, vat, total_amount):
    """This is the function to generate invoice after selling furniture to the customer"""
    print("Sell invoice has been generated")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    time = datetime.datetime.now().strftime("%H:%M:%S")
    date_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    receipt_name = f"""{cus_name.lower().replace(" ", "")}sell-receipt{date_time}.txt"""

    uni_sell_details = f"""
    {"----------------------------------------------------Sell receipt---------------------------------------------------":^110}

    {"BRJ Furniture Store":<60} {"Date of purchase: "}{date} 
    {"SundarHaraincha-07,Gothgaun,Morang":<60} Time of purchase: {time} 
    {"PHONE- +977-9819394472 ":<60} Name of employee(Purchaser): {cus_name}  
    {"ESTD.- 2059 BS":<60} Location: {location}
    Invoice num: {datetime.datetime.now().strftime("%H%M%S"):<47} Phone No: {ph_no} 
                                                    

    |{"SN":^3} | {"ID":^3} | {"Furniture Name":^15} | {"Manufacturer":^30} | {"Quantity":^10} | {"Price/unit":^12} | {"Total":^10}|     
    """

    multi_sell_details = f""""""
    multi_sell_total = 0
    total_vat = 0
    for sell_count in range(len(product_id)):
        multi_sell_total += total_amount[sell_count]
        total_vat += vat[sell_count]
        multi_sell_details += f"""
    |{sell_count+1:<3} | {product_id[sell_count]:<3} | {product_name[sell_count]:<15} | {manufacturer[sell_count]:<30} | {quantity[sell_count]:<10} | ${price_per_unit[sell_count]:<11} | ${total_amount[sell_count]:<9}|
        """
    
        
    final_sell_details = f"""{uni_sell_details} {multi_sell_details} 
    {"|":>76} {"Sub-Total:":<12} | {"$":>1}{multi_sell_total:<9}|
    {"|":>76} {"VAT:":<12} | {"$":>1}{total_vat:<9}|
    {"|":>76} {"Shipping:":<12} | {"$":>1}{shipping_cost:<9}|
    {"|":>76} {"Grand total:":<11} | {"$":>1}{multi_sell_total + shipping_cost + total_vat:<9}|"""
    print(final_sell_details)

    with open(receipt_name, "w") as receipt:
        receipt.write(final_sell_details)

        