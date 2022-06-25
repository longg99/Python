from cgitb import text
from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.autotrader.ca/" +
                         "cars/on/toronto/?rcp=0&rcs=0&prx=100" +
                         "&prv=Ontario&loc=Toronto%2C%20ON&hprc=True&wcp=True&iosp=True&sts=New-Used&inMarket=basicSearch&make=Honda").text

print(html_text)
