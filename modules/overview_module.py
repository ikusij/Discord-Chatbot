import modules.price_module as price_module
import modules.utility as utility

def format_row(header, value, padding_left = 20, padding_right = 15):
    return f'{header:<{padding_left}}{value:>{padding_right}}'

def format_column(json_data, keys, path):
    
    column = []
    
    for key, header in keys.items():
        value = utility.fetch_value_by_path(json_data, path.format(key = key))
        row = format_row(header, value)
        column.append(row)

    return column

def console(json_data):

    keys = utility.fetch_format_data("./format/overview.json")
    
    left_column = keys["leftColumn"]
    left_column_path = keys["paths"]["leftColumnPath"]

    left_column_formatted = format_column(json_data, left_column, left_column_path)

    right_column = keys["rightColumn"]
    right_column_path = keys["paths"]["rightColumnPath"]

    right_column_formatted = format_column(json_data, right_column, right_column_path)

    table = f'{price_module.console(json_data)}\n'

    for x in range(len(left_column_formatted)):

        table += f'`{left_column_formatted[x]}`'

        if x < len(right_column_formatted):
            table += f' | '
            table += f'`{right_column_formatted[x]}`'
        
        table += '\n'
    
    return table