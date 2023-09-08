import csv, os
from conftest import RESOURCES_DIR

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

def test_csv():
    csv_file_path = os.path.join(RESOURCES_DIR, 'new_csv.csv')
    with open(csv_file_path, 'w', newline="") as csv_file:
        csvwriter = csv.writer(csv_file, delimiter=';')
        csvwriter.writerow(['Bonny', 'Born', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(csv_file_path) as csv_file:
        file_rows = []
        csvreader = csv.reader(csv_file, delimiter=';')
        for row in csvreader:
            file_rows.append(row)

    assert file_rows[0] == ['Bonny', 'Born', 'Peter']
    assert file_rows[1] == ['Alex', 'Serj', 'Yana']