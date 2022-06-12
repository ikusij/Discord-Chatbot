import modules.utility as utility

def fetch_current_price(json_data):
    format_data = utility.fetch_format_data("./format/alert.json")
    key = format_data["key"]
    path = format_data["path"]
    current_price = utility.fetch_value_by_path(json_data, path.format(key = key))
    return current_price

def add_alert_price(ticker, alert_price, alert_prices):
    alert_prices[ticker] = alert_price

def remove_alert_price(ticker, alert_prices):
    alert_prices.pop(ticker)

def check_alert_above(current_price, alert_price):
    return alert_price < current_price

def message_alert_above(ticker, current_price, alert_price):
    return f'{ticker} is above ${alert_price:.2f}. Current price: ${current_price:.2f}'

def check_alert_below(current_price, alert_price):
    return alert_price > current_price

def message_alert_below(ticker, current_price, alert_price):
    return f'{ticker} is below ${alert_price:.2f}. Current price: ${current_price:.2f}'

def check_above(current_price, alert_prices_above):
    
    messages = []

    tmp = alert_prices_above.copy()
    
    for ticker, alert_price in alert_prices_above.items():
        if check_alert_above(current_price, alert_price):
            messages.append(message_alert_above(ticker, current_price, alert_price))
            remove_alert_price(ticker, tmp)

    print(tmp)
    alert_prices_above = tmp
    print(alert_prices_above)

    return messages

def check_below(current_price, alert_prices_below):
    
    messages = []
    
    for ticker, alert_price in alert_prices_below.items():
        if check_alert_below(current_price, alert_price):
            messages.append(message_alert_below(ticker, current_price, alert_price))
            remove_alert_price(ticker, alert_prices_below)

    return messages