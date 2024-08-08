import os
import time

# Задайте каталог для поиска (текущий каталог)
directory = "."


# Функция для вывода информации о файлах
def print_file_info(directory):
    # Проходим по всем каталогам и файлам в указанном каталоге
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Формируем полный путь к файлу
            filepath = os.path.join(root, file)

            # Получаем время последнего изменения файла
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

            # Получаем размер файла
            filesize = os.path.getsize(filepath)

            # Получаем родительскую директорию файла
            parent_dir = os.path.dirname(filepath)

            # Выводим информацию о файле
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


# Вызов функции
print_file_info(directory)