import requests
from bs4 import BeautifulSoup
import json
import time
from credentials import getCredentials
import tweepy


page = requests.get("https://www.worldometers.info/coronavirus/country/brazil/")
soup = BeautifulSoup(page.text, 'html.parser')

container = soup.findAll("div", {"class": "maincounter-number"})
cases = container[0].text.strip()
deaths = container[1].text.strip()
recovered = container[2].text.strip() 

brasil = ("🇧🇷 Total de casos no Brasil: \n"+ \
        "Casos confirmados: " + cases + "\n" + \
        "Óbitos: " + deaths+ "\n" + \
        "Recuperações: " + recovered + "\n\n")

page = requests.get("https://www.worldometers.info/coronavirus/")
soup = BeautifulSoup(page.text, 'html.parser')

container = soup.findAll("div", {"class": "maincounter-number"})
cases = container[0].text.strip()
deaths = container[1].text.strip()
recovered = container[2].text.strip() 

mundo = ("🌍 Total de casos no Mundo: \n"+ \
        "Casos confirmados: " + cases + "\n" + \
        "Óbitos: " + deaths+ "\n" + \
        "Recuperações: " + recovered + "\n\n")

print(brasil)
print(mundo)
hashtag = "#coronavirus #corona #covid19 #coronavirusbrasil"

api = getCredentials('twitter')
update = api.update_with_media("world.jpg", brasil + "\n" + mundo + "\n" + hashtag )
print(update)
