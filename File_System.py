# Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
# Примените os.path.join для формирования полного пути к файлам.
# Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
# Используйте os.path.getsize для получения размера файла.
# Используйте os.path.dirname для получения родительской директории файла.


import time
import os

directory = 'C:\pythonProject\Modul7'

for root, dirs, files in os.walk(directory):
    print('+' * 28)
    print(root, dirs, files)
    print('+' * 28)
    for file in files:
        print('-' * 50)
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
        print(
            f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}'
        )
