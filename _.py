import requests
from bs4 import BeautifulSoup
import csv
from concurrent.futures import ThreadPoolExecutor
import threading

base_url = "https://www.olx.uz/uslugi/"

def parse_page(page_num):
    url = base_url + "?page=" + str(page_num)
    response = requests.get(url)
    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        href_values = [a['href'] for a in soup.find_all('a', class_='css-z3gu2d')]
        # print(f"Обрабатывается страница {page_num}")
        return href_values
    else:
        # print("Не удалось выполнить запрос для страницы", page_num)
        return []

def write_to_csv(data):
    with lock:
        writer.writerow(data)

lock = threading.Lock()

with open('end.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    with ThreadPoolExecutor() as executor:
        all_href_values = executor.map(parse_page, range(1, 10000))
        
        for page_num, href_values in enumerate(all_href_values, start=1):
            for href in href_values:
                write_to_csv([href])
            print(f"Обработка страницы {page_num} завершена")

print("Спарсено ссылок и сохранено в файл 'olx_links.csv'")

