from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.kijijiautos.ca/cars/sedan/").text

soup = BeautifulSoup(html_text, 'html.parser')
cars = soup.find_all("div", class_='b1yLWE bcN7dZ')
for car in cars:
    car_name = car.find("h2", class_="G2jAym fcN7dZ z2jAym p2jAym b2jAym").text
    price = car.find(
        "span", class_="G2jAym d3uM7V C2jAym p2jAym b2jAym").text.replace("*", "")
    # link = car.find('a', class_="bcNN7t").text

    print(f'''
    Car name: {car_name}
    Price: {price} 
    ''')
