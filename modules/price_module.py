import modules.utility as utility

def format_name_full(name_full):
    return f'{name_full} '

def format_ticker(ticker):
    return f'({ticker})'

def fetch_company_info(json_data, format_data):
    
    company_information_keys = format_data["companyInformation"]
    path = format_data["paths"]["companyInformationPath"]

    text = ""
    
    for key in company_information_keys.keys():
        
        value = utility.fetch_value_by_path(json_data, path.format(key = key))

        if key == "nameFull":
            value = format_name_full(value)
            text += value
        elif key == "ticker":
            value = format_ticker(value)
            text += value
    
    return text

def format_p(price):
    return f'${price:.2f} '

def format_c(price_change):
    price_change = float(price_change)
    if price_change > 0:
        return f'+{price_change:.2f} '
    else:
        return f'{price_change:.2f} '

def format_cp(price_change_percent):
    price_change_percent = float(price_change_percent)
    if price_change_percent > 0:
        return f'(+{price_change_percent:.2f}%)'
    else:
        return f'({price_change_percent:.2f}%)'

def fetch_price_info(json_data, format_data):

    price_information_keys = format_data["priceInformation"]
    path = format_data["paths"]["priceInformationPath"]

    text = ""
    
    for key in price_information_keys.keys():
        
        value = utility.fetch_value_by_path(json_data, path.format(key = key))

        if key == "p":
            value = format_p(value)
            text += value
        elif key == "c":
            value = format_c(value)
            text += value
        elif key == "cp":
            value = format_cp(value)
            text += value
    
    return text

def console(json_data):
    format_data = utility.fetch_format_data("./format/price.json")
    company_info = fetch_company_info(json_data, format_data)
    price_info = fetch_price_info(json_data, format_data)
    message = f'`{company_info} -- {price_info}`'
    return message