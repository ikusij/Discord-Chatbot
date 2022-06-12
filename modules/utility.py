import bs4
import json
import dotenv
import modules.headers as headers
import requests

def fetch_html(url):
    raw_response = requests.get(url, headers = headers.headers)
    response = raw_response.text
    html = bs4.BeautifulSoup(response, 'lxml')
    return html

def fetch_json(html):
    tag = html.find('script', type = 'application/json')
    script = tag.text
    json_data = json.loads(script)
    return json_data

def fetch(url):
    html = fetch_html(url)
    json_data = fetch_json(html)
    return json_data

def fetch_api_key():
    config = dotenv.dotenv_values('.env')
    api_key = config['API_KEY']
    return api_key

def fetch_format_data(filename):
    with open(filename, 'r') as file:
        format_data = json.load(file)
    return format_data

def fetch_value_by_path(json_data, path, path_delimiter = '/'):
    for key in path.split(path_delimiter):
        json_data = json_data[key]
    return json_data