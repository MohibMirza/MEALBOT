import urllib2
from re import compile
from bs4 import BeautifulSoup
import requests

URL = "https://hospitality.usc.edu/residential-dining-menus/"

r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser')

def find_food(food):
	s = "";
	if food in soup.find_all('div', 'hsp-accordian-container')
		s = "They are serving " + food + " today!"
	return s;