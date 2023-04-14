import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
COMPANY_ID = os.getenv("COMPANY_ID")
PASSWORD = os.getenv("PASSWORD")
YANDEX_BASE_URL = os.getenv("BASE_URL")
FROM_EMAIL = os.getenv("EMAIL")
SENDER_EMAIL_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")


BASE_URL = YANDEX_BASE_URL + COMPANY_ID

api_request_headers = {"Authorization": "OAuth " + TOKEN}
