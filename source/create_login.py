from letters import letter_collection


def generate_named_login(last_name: str, first_name: str) -> str:
    """Return email login based on first and last cyrillic names of a user"""
    last_name_transliterated = ""
    for cyrilic_letter in last_name:
        latin_letter = str(letter_collection.get(cyrilic_letter))
        last_name_transliterated += latin_letter

    named_login = (
        str(letter_collection.get(first_name[0])) + "." + last_name_transliterated
    )
    return named_login


if __name__ == "__main__":
    fname = input("Введите имя пользователя: ")
    lname = input("Ввведите фамилию пользователя: ")
    output = generate_named_login(lname.upper(), fname.upper())
    print(output.lower())
