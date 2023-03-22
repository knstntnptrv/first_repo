from bs4 import BeautifulSoup
import requests

url = 'https://beautiful-soup-4.readthedocs.io/en/latest/#installing-beautiful-soup'

response = requests.get(url)
bs = BeautifulSoup(response.text, 'lxml')
temp = bs.find('span', 'temp__value temp__value_with-unit')
print(temp.get_text())
