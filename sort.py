# import csv

# # Чтение ссылок из файла
# with open('_________________.csv', 'r', newline='', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     # Создание множества для хранения уникальных ссылок
#     unique_links = set(row[0] for row in reader)

# # Сортировка и преобразование обратно в список
# sorted_unique_links = sorted(unique_links)

# # Перезапись отсортированных уникальных ссылок в файл
# with open('__-------________.csv', 'a', newline='', encoding='utf-8') as csvfile:
#     writer = csv.writer(csvfile)
#     for link in sorted_unique_links:
#         writer.writerow([link])


# print("Ссылки отсортированы и удалены дубликаты.")

import csv

# Открываем существующий файл и читаем его содержимое
with open('__-------________.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    # Преобразуем содержимое в список строк
    rows = list(reader)

# URL-адрес, который нужно добавить в начало каждой строки
base_url = "https://www.olx.uz"

# Добавляем новое значение к началу каждой строки
for row in rows:
    # Проверяем, что значение начинается с "/"
    if row[0].startswith("/"):
        row[0] = base_url + row[0]

# Перезаписываем файл с обновленными строками
with open('existing_file.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Записываем обновленные строки в файл
    writer.writerows(rows)
