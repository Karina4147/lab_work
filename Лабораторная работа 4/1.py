# TODO импортировать необходимые модули
import csv
import json
import collections

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with (open(INPUT_FILENAME, 'r', encoding="utf-8") as file,
          open(OUTPUT_FILENAME, 'w', encoding="utf-8") as f):

        reader = csv.DictReader(file)  # TODO считать содержимое csv файла
        result = [d for d in reader]
        f.write(json.dumps(result, indent=4))

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME, encoding="utf-8") as output_f:
        for line in output_f:
            print(line, end="")
