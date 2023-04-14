import re


def check_cyrillic(name: str) -> bool:
    pattern = "[\u0400-\u04FF]"
    try:
        evaluation_result = bool(re.search(pattern, name))
        if not evaluation_result:
            raise ValueError
    except ValueError:
        print("Требуется кириллический текст")
    return evaluation_result


def check_latin(name: str) -> bool:
    pattern = "^[a-z0-9\-_.]+$"
    try:
        evaluation_result = bool(re.search(pattern, name))
        if not evaluation_result:
            raise ValueError
    except ValueError:
        print("Требуется латинский текст строчными буквами без специальных символов")
    return evaluation_result


def check_phone_number(phone: str) -> bool:
    pattern = "^\+[3][7][5]\d{9}"
    try:
        evaluation_result = bool(re.search(pattern, phone))
        if not evaluation_result:
            raise ValueError
    except ValueError:
        print("Требуется ввести номер в формате +375 ХХ ХХХ ХХ ХХ")
    return evaluation_result


def check_email(email: str) -> bool:
    pattern = "^\S+@\S+\.\S+$"
    try:
        evaluation_result = bool(re.fullmatch(pattern, email))
        print(evaluation_result)
        if not evaluation_result:
            raise ValueError
    except ValueError:
        print("Требуется ввести валидный email")
    return evaluation_result


def handle_user_inputs(input_text: str) -> str:
    while True:
        user_data = input(input_text)
        if check_cyrillic(user_data):
            break
    return user_data


def handle_initiator_email(email: str) -> str:
    while True:
        e = input(email)
        if check_email(e):
            break
    return e


def handle_login(login_input) -> str:
    while True:
        l = input(login_input)
        if check_latin(l):
            break
    return l.lower()


def handle_dept_input(dept_input):
    while True:
        v = int(input(dept_input))
        if isinstance(v, int) and (v in range(1, 18)):
            break
        else:
            print(
                (
                    f"Используйте числовую клавиатуру для ввода номера подразделения.\n"
                    f"Номера подразделений в списке выше, левая колонка"
                )
            )
    return v


def handle_input_options(input_text):
    INPUT_OPTIONS = ["да", "нет"]
    input_option = input(input_text)
    while input_option not in INPUT_OPTIONS:
        print("Введите либо 'да', либо 'нет'")
        input_option = input(input_text)
    else:
        return input_option


def format_phone_number(n: str) -> str:
    ommited_characters = [" ", "-", "(", ")"]
    for el in ommited_characters:
        n = n.replace(el, "")
    number_chunks = [n[:4], n[4:6], n[6:9], n[9:11], n[11:13]]
    return " ".join(number_chunks)


def handle_phone_input(phone_input):
    while True:
        v = input(phone_input)
        if check_phone_number(v.replace(" ", "")):
            formatted_number = format_phone_number(v)
            break
    return formatted_number
