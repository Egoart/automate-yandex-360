from letters import letter_collection


def generate_named_login(last_name: str, first_name: str) -> str:
    last_name_transliterated = ""
    for cyrilic_letter in last_name:
        latin_letter = str(letter_collection.get(cyrilic_letter))
        last_name_transliterated += latin_letter

    named_login = (
        str(letter_collection.get(first_name[0])) + "." + last_name_transliterated
    )
    return named_login
