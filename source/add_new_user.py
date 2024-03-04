import datetime
import requests

from utils import BASE_URL
from utils import api_request_headers as headers
from utils import timeout

from create_password import create_password

from create_users_list import generate_users_list
from send_mail import send_mail_to_initiator


URL = BASE_URL + "/users/"


def handle_timestamp(api_dates) -> list:
    processed_dates = []
    for date in api_dates:
        d = date.removesuffix("Z")
        processed_dates.append(datetime.datetime.fromisoformat(d).strftime("%d/%m/%y"))
    return processed_dates


def check_department_id(user_data):
    dept_id = user_data.get("department_id")
    if not (dept_id or isinstance(dept_id, int)):
        return 1
    else:
        return dept_id


def create_user(user_data):
    request_body = {
        "departmentId": check_department_id(user_data),
        "name": {
            "first": user_data.get("first_name"),
            "last": user_data.get("last_name"),
            "middle": user_data.get("middle_name"),
        },
        "nickname": user_data.get("login"),
        "password": create_password(),
        "position": user_data.get("position"),
        "timezone": "Europe/Minsk",
        "contacts": [{"type": "phone", "value": user_data.get("phone")}],
        "passwordChangeRequired": True,
    }
    api_response = requests.post(
        URL, headers=headers, json=request_body, timeout=timeout
    )

    if api_response.status_code != 200:
        message = api_response.json()["message"]
        print(
            f"Не удалось создать аккаунт пользователя. Код ответа {api_response.status_code}. Детали: {message}"
        )
    elif api_response.status_code == 200:
        api_user_data = {
            "last_name": api_response.json()["name"]["last"],
            "first_name": api_response.json()["name"]["first"],
            "middle_name": api_response.json()["name"]["middle"],
            "position": api_response.json()["position"],
            "email": api_response.json()["email"],
            "timestamps_list": [
                api_response.json()["createdAt"],
                api_response.json()["updatedAt"],
            ],
            "password": request_body["password"],
        }
        send_mail_to_initiator(user_data, api_user_data)
        print(
            f"\n"
            f"Добавлен новый контакт: {api_user_data['last_name']} "
            f"{api_user_data['first_name']} "
            f"{api_user_data['middle_name']}, "
            f"{api_user_data['position'].lower()}"
            f"\n"
        )
        print(api_user_data["email"])
        formatted_dates = handle_timestamp(api_user_data["timestamps_list"])
        print(
            f"Этот адрес создан {formatted_dates[0]}, модифицирован {formatted_dates[1]}."
        )
        generate_users_list()
        print(f"Детали контакта:\n {api_response.json()}")
