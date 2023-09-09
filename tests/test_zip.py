import zipfile, os
from tests.conftest import RESOURCES_DIR

def test_zip():
    archive_zip = os.path.join(RESOURCES_DIR, 'tmp.zip')
    with zipfile.ZipFile(archive_zip, 'r') as zip_file:
        print(f'Содержимое архива: {zip_file.namelist()}')


