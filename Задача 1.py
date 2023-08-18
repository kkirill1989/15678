#Напишите функцию, которая сереализует содержимое текущей директории в json-файл. 
#В файле должен храниться список словарей, словарь описывает элемент внутри директории: имя, расширение, тип. 
#Если элемент - директория, то только тип и имя. 
#Пример результата для папки, где лежит файл test.txt и директория directory_test:
#[
#{
#'name': 'test',
#'extension': '.txt',
#'type': 'file'
#},
#{
#'name': 'directory_test',
#'type': 'directory',
#}
#]

import csv
import json
import os
from pathlib import Path


def get_from_user(file: Path) -> None:
    json_file = {}
    if os.path.isfile(file):
        with open(file, 'r', encoding='utf-8') as js:
            if os.path.getsize(file) > 0:
                json_file = json.load(js)

    rows = []
    for level, value in json_file.items():
        for id, name in value.items():
            rows.append({'level': level, 'user_id': id, 'name': name})

    with open('out.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['level', 'user_id', 'name']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    get_from_user(Path('./names.json'))