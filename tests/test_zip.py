import zipfile, os
from tests.conftest import RESOURCES_DIR

files_to_zip = os.listdir(RESOURCES_DIR)
def test_zip():
    with zipfile.ZipFile(os.path.join(RESOURCES_DIR, 'tmp.zip'), 'w') as zip_file:
        for file_to_zip in files_to_zip:
            file_path = os.path.join(RESOURCES_DIR, file_to_zip)
            zip_file.write(file_path, file_to_zip)
        name_list = zip_file.namelist()
        print(f'Содержимое архива: {name_list}')

    assert name_list == files_to_zip

    os.remove(os.path.join(RESOURCES_DIR, 'tmp.zip'))