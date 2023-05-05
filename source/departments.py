import requests

from utils import BASE_URL as URL
from utils import api_request_headers as headers
from utils import timeout

URL_DEPTS = URL + "/departments/" + "?page=1&perPage=30"


def fetch_depatments() -> dict:
    api_response_departments = requests.get(URL_DEPTS, headers=headers, timeout=timeout)
    dept_key_list = []
    dept_value_list = []
    for department in api_response_departments.json()["departments"]:
        dept_key_list.append(department["id"])
        dept_value_list.append(department["name"])
    return dict(zip(dept_key_list, dept_value_list))


if __name__ == "__main__":
    fetch_depatments()
