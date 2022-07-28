from bs4 import BeautifulSoup
import requests
import re

# html_text = requests.get("https://www.kijijiautos.ca/cars/sedan/").text

# soup = BeautifulSoup(html_text, 'lxml')
# # cars = soup.find_all("div", class_='b1yLWE bcN7dZ')
# # for car in cars:
# #     car_name = car.find("h2", class_="G2jAym fcN7dZ z2jAym p2jAym b2jAym").text
# #     price = car.find(
# #         "span", class_="G2jAym d3uM7V C2jAym p2jAym b2jAym").text.replace("*", "")

# car_sections = soup.find_all(attrs={'data-testid': 'SearchResultListItem'})

# for a in soup.find_all('a', attrs={'class': 'bcNN7t'}):
#     print(a)
# for car_section in car_sections:
#     cars = car_section.find_all("a", class_='b1yLWE bcN7dZ')
#     for car in cars:
#         car_name = car.find(
#             "h2", class_="G2jAym fcN7dZ z2jAym p2jAym b2jAym").text
#         price = car.find(
#             "span", class_="G2jAym d3uM7V C2jAym p2jAym b2jAym").text.replace("*", "")

#     # print(car_name + ": " + price)

vnexpress_text = requests.get("https://vnexpress.net/").text
soup_2 = BeautifulSoup(vnexpress_text, 'lxml')
news = soup_2.find_all('h3', class_="title-news")
for item_news in news:
    news_title = item_news.find('a')
    print("Title: " + news_title.get('title') +
          ", link: " + news_title.get('href'))
