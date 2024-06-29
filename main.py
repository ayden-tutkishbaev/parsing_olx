import requests
from bs4 import BeautifulSoup
from database import *

URL = 'https://www.olx.uz/'

create_categories_table()
create_goods_table()

html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')

categories_block = soup.find('div', class_='css-1rwzo2t')

categories = categories_block.find_all('a', class_='css-1gpccxq')
categories2 = categories_block.find_all('a', class_='css-o73al1')

for category in categories: # Первый ряд товаров

    category_link = 'https://www.olx.uz' + category.get('href')

    if category_link != 'https://www.olx.uz/rabota/':  # Пропускаем раздел "Работа" из-за его своеобразности

        category_title = category.get_text(strip=True)
        save_category(category_title)
        category_id = get_category_id(category_title)
        new_html = requests.get(category_link).text
        new_soup = BeautifulSoup(new_html, 'html.parser')

        goods_list = new_soup.find('div', {'class': 'css-oukcj3'})
        goods = goods_list.find_all('div', class_='css-1sw7q4x')

        for good in goods:
            good_title = good.find('h6', class_='er34gjf0').get_text()
            good_link = 'https://www.olx.uz' + good.find('a', class_='css-rc5s2u').get('href')
            good_price = good.find('p', 'er34gjf0').get_text()
            good_location1 = good.find('p', {'data-testid': 'location-date'}).get_text()
            good_location = good_location1.rpartition(' - ')[0]
            print(category.get_text())
            print(good_title)
            print(good_link)
            str(good_price)
            print(good_price)
            print(good_location)
            print()
            save_good(category_id=category_id, good_title=good_title, good_link=good_link, good_price=good_price,
                      good_location=good_location)

for category in categories2: # Второй ряд товаров

    category_link = 'https://www.olx.uz' + category.get('href')

    if category_link != 'https://www.olx.uz/rabota/':

        category_title = category.get_text(strip=True)
        save_category(category_title)
        category_id = get_category_id(category_title)
        new_html = requests.get(category_link).text
        new_soup = BeautifulSoup(new_html, 'html.parser')

        goods_list = new_soup.find('div', {'class': 'css-oukcj3'})
        goods = goods_list.find_all('div', class_='css-1sw7q4x')

        for good in goods:
            good_title = good.find('h6', class_='er34gjf0').get_text()
            good_link = 'https://www.olx.uz' + good.find('a', class_='css-rc5s2u').get('href')
            good_price = good.find('p', 'er34gjf0').get_text()
            good_location1 = good.find('p', {'data-testid': 'location-date'}).get_text()
            good_location = good_location1.rpartition(' - ')[0]
            print(category.get_text())
            print(good_title)
            print(good_link)
            str(good_price)
            print(good_location)
            print()
            save_good(category_id=category_id, good_title=good_title, good_link=good_link, good_price=good_price,
                      good_location=good_location)

# Выполнено Айденом Туткишбаевым 光