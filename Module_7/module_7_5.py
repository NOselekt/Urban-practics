import os
import time

directory = '.'
os.chdir(directory)
for root, dirs, files in os.walk(directory):
    for file in files:
        path = os.path.join(root, file)
        size = os.path.getsize(path)
        last_redaction_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(os.path.getmtime(path)))
        parent_directory = os.path.dirname(path)
        print(f"Обнаружен файл: {file}, путь: \"{path}\", родительская директория: \"{parent_directory}\", "
              f"размер: {size} байт, "
              f"время последнего редактирования: {last_redaction_time}")


