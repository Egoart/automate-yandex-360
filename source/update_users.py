import requests

from add_new_user import BASE_URL
from utils import api_request_headers as headers
from utils import timeout
from validations import handle_email
from validations import handle_phone_input


URL_USERS = BASE_URL + "/users/" + "?page=1&perPage=200"


def obtain_user_data() -> dict:
    user_number = int(
        input(
            "Введите число пользователей, которым необходимо изменить контактный номер: "
        )
    )

    user_data = {}
    for user in range(user_number):
        user_data.update(
            {
                handle_email(
                    f"Введите email пользователя {user+1}: "
                ): handle_phone_input(
                    f"Введите новый номер телефона в формате +375 ХХ ХХХ ХХ ХХ пользователя {user+1}: "
                )
            }
        )
    return user_data


def update_user_contact_info():
    api_response = requests.get(URL_USERS, headers=headers)

    users_dict_list = [
        {
            "user_id": user["id"],
            "last_name": user["name"]["last"],
            "first_name": user["name"]["first"],
            "middle_name": user["name"]["middle"],
            "user_email": user["email"],
        }
        for user in api_response.json()["users"]
    ]

    user_new_data = obtain_user_data()

    for user in users_dict_list:
        if user["user_email"] in user_new_data.keys():
            user_id = user["user_id"]
            URL_USER_ID = BASE_URL + "/users/" + user_id + "/contacts"
            request_body = {
                "contacts": [
                    {
                        "type": "phone",
                        "value": user_new_data.get(user["user_email"]),
                    }
                ]
            }
            r = requests.put(
                URL_USER_ID, headers=headers, json=request_body, timeout=timeout
            )
            print(f"Для пользователя {user} ответ сервера {r.json()}")


if __name__ == "__main__":
    update_user_contact_info()
