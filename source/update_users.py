import requests

from add_new_user import BASE_URL
from add_new_user import api_request_headers
from update_data_source import email_phone_dict as data_source


URL_USERS = BASE_URL + "/users/" + "?page=1&perPage=200"


def update_user_contact_info():

    api_response = requests.get(URL_USERS, headers=api_request_headers)

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

    for user in users_dict_list:
        if user["user_email"] in data_source.keys():
            user_id = user["user_id"]
            URL_USER_ID = BASE_URL + "/users/" + user_id + "/contacts"
            request_body = {
                "contacts": [
                    {"type": "phone", "value": data_source.get(user["user_email"])}
                ]
            }
            r = requests.put(
                URL_USER_ID, headers=api_request_headers, json=request_body
            )
            print(r.json())


if __name__ == "__main__":
    update_user_contact_info()
