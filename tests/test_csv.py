import csv, os
from conftest import RESOURCES_DIR

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_csv():
    csv_file_path = os.path.join(RESOURCES_DIR, 'new_csv.csv')
    with open(csv_file_path, 'w') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_file_path) as csv_file:
        row = []
        csvreader = csv.reader(csv_file, delimiter=';')
        for row in csvreader:
            row.append()

    assert row[0] == ['Bonny', 'Born', 'Peter']
    assert row[1] == ['Alex', 'Serj', 'Yana']