import requests
from requests.exceptions import ConnectTimeout
import xlsxwriter
from functools import reduce
from operator import add


from utils import BASE_URL as URL
from utils import api_request_headers as headers
from utils import get_or_create_file_path
from utils import timeout
from departments import fetch_depatments


URL_USERS = URL + "/users/" + "?page=1&perPage=200"


def phone_from_json(user) -> str:
    if user["contacts"][0]["type"] == "phone":
        return user["contacts"][0]["value"]
    else:
        return f"не указан"


def count_items_in_user(users_list) -> int:
    len_list = [len(user) for user in users_list]
    el_sum = reduce(add, len_list)
    avrg_len = el_sum / len(users_list)
    return int(avrg_len)


def users_to_excel(users_list):
    column_titles_list = [
        "Фамилия",
        "Имя",
        "Отчество",
        "email",
        "Телефон",
        "Должность",
        "Подразделение",
    ]

    # create Excel file and worksheet
    file_name = get_or_create_file_path("emails_list.xlsx")

    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()
    # format first row with bold characters
    bold = workbook.add_format({"bold": True})

    if len(column_titles_list) != count_items_in_user(users_list):
        print(
            f"Количество столбцев не соответствует количеству записей для пользователя"
        )
    else:
        # create first_row
        for col_num, title in enumerate(column_titles_list):
            worksheet.write(0, col_num, title, bold)

        for row_num, row_data in enumerate(users_list, start=1):
            for col_num, col_data in enumerate(row_data):
                worksheet.write(row_num, col_num, col_data)

        # fit column width to content
        worksheet.autofit()
        workbook.close()
        print(f"Список пользователей обновлен в файле {file_name}")


def generate_users_list():
    api_response = requests.get(URL_USERS, headers=headers, timeout=timeout)
    department_dict = fetch_depatments()
    users_list = [
        [
            user["name"]["last"],
            user["name"]["first"],
            user["name"]["middle"],
            user["email"],
            phone_from_json(user),
            user["position"],
            department_dict.get(user["departmentId"]),
        ]
        for user in api_response.json()["users"]
    ]

    # slicing is used to remove service emails from list
    users_list_excl_service_emails = users_list[5:]
    users_to_excel(users_list_excl_service_emails)


if __name__ == "__main__":
    generate_users_list()
