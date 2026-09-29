import requests
from bs4 import BeautifulSoup

url = 'http://www.bu.edu/president/boston-university-facts-stats/'
response = requests.get(url)
content= response.content
soup = BeautifulSoup(content, 'html.parser')




