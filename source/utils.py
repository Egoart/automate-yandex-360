import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

TOKEN = os.getenv("TOKEN")
COMPANY_ID = os.getenv("COMPANY_ID")
PASSWORD = os.getenv("PASSWORD")
YANDEX_BASE_URL = os.getenv("BASE_URL")
FROM_EMAIL = os.getenv("EMAIL")
SENDER_EMAIL_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")


BASE_URL = YANDEX_BASE_URL + COMPANY_ID

api_request_headers = {"Authorization": "OAuth " + TOKEN}

timeout = 2


def get_or_create_file_path(file_name):
    cdw = Path(__file__).absolute().parent

    # Directory in parent folder to contain Excel files
    exls_dir_name = "data_files"

    data_dir_path = os.path.join(cdw, exls_dir_name)
    if not os.path.exists(data_dir_path):
        os.makedirs(data_dir_path)
        print(
            f"Создана директория для размещения файлов Excel под названием {exls_dir_name}"
        )
    return os.path.join(data_dir_path, file_name)
