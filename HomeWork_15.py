import os
from collections import namedtuple
import logging


def get_directory_info(file_path):
    Directory = namedtuple('Directory', ['name', 'extension', 'is_directory', 'parent_directory'])
    directory_info = []

    for item in os.listdir(file_path):
        item_path = os.path.join(file_path, item)
        is_directory = os.path.isdir(item_path)
        parent_directory = os.path.basename(os.path.dirname(item_path))

        if is_directory:
            name = item
            extension = None
        else:
            name, extension = os.path.splitext(item)

        directory_info.append(Directory(name, extension, is_directory, parent_directory))

    return directory_info


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Получение информации о директории.')
    parser.add_argument('file_path', type=str, help='Путь к директории')

    args = parser.parse_args()

    if args.file_path:
        logging.basicConfig(filename='directory_info.log', filemode="w",encoding="UTF-8", level=logging.INFO)
        logging.info(get_directory_info(args.file_path))
    else:
        print("Вы не указали путь к директории в качестве аргумента командной строки.")