import requests
import re
from bs4 import BeautifulSoup
import mysql.connector as connector


def fetch_data(number):
    URL = f"https://www.truecar.com/used-cars-for-sale/listings/?page={number}"
    r = requests.get(URL)
    data = BeautifulSoup(r.text, 'html.parser')
    car_data = data.find_all('div', {"data-test": "cardContent"})
    return (car_data)


def get_car_name(inputed_data):
    name = inputed_data.find(
        'span', {'class': "truncate"}).get_text(strip=True)
    return (name.lower())


def get_car_year(inputed_data):
    year = inputed_data.find(
        'span', {'class': "vehicle-card-year text-xs"}).get_text(strip=True)
    year = int(year)
    return (year)


def get_car_mileage(inputed_data):
    mile = inputed_data.find(
        'div', {'data-test': "vehicleMileage"}).get_text(strip=True)
    mile = re.findall(r'(.*)miles', mile)
    mile = (mile[0].replace(',', '')).strip()
    mile = int(mile)
    return mile


def get_car_accident(inputed_data):
    accident_status = inputed_data.find(
        'div', {'data-test': "vehicleCardCondition"}).get_text(strip=True)
    accident_status = re.findall(r'(.*) accident', accident_status)
    if accident_status[0] == 'No':
        accident_status = 0
    else:
        accident_status = int(accident_status[0].strip())
    return (accident_status)


def get_car_owner(inputed_data):
    owener_status = inputed_data.find(
        'div', {'data-test': "vehicleCardCondition"}).get_text(strip=True)
    owner_status = re.findall(r',(.*)Owner', owener_status)
    owner_status = int(owner_status[0].strip())
    return (owner_status)


def get_car_color(inputed_data):
    color_deafalt = inputed_data.find(
        'div', {'data-test': "vehicleCardColors"}).get_text(strip=True)
    color_deafalt = color_deafalt.lower()
    color_deafalt = re.findall(r'(.*)exterior', color_deafalt)
    color_deafalt = color_deafalt[0]
    return (color_deafalt)


def get_car_price(inputed_data):
    car_price = inputed_data.find(
        'span', {'data-test': "vehicleListingPriceAmount"}).get_text(strip=True)
    car_price = re.findall(r'\$(.*)$', car_price)
    car_price = int(car_price[0].replace(',', ''))
    return (car_price)


cnx = connector.connect(
    user='root', password='password', host='', database='')
cursor = cnx.cursor()


def input_in_database(name, year, mile, accident, owner, color, price, page):
    cursor.execute(
        f"INSERT INTO car_datas VALUES('{name}',{year},{mile},{accident},{owner},'{color}',{price},{page});")
    cnx.commit()


page_counter = 301
while page_counter <= 333:

    all_data_car = fetch_data(page_counter)

    for card in all_data_car:

        car_name = get_car_name(card)  # string
        car_year = get_car_year(card)  # int
        car_mileage = get_car_mileage(card)  # int
        car_accident = get_car_accident(card)  # int
        car_owner = get_car_owner(card)  # int
        car_color = get_car_color(card)  # string
        car_price = get_car_price(card)  # int

        input_in_database(car_name, car_year, car_mileage,
                          car_accident, car_owner, car_color, car_price, page_counter)

    page_counter += 1
