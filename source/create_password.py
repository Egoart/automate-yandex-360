import random
from secrets import choice
import string

LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL = string.punctuation


def create_password():
    grouped_symbols = LETTERS + DIGITS
    while True:
        random_password = "".join(choice(grouped_symbols) for s in range(11))
        if (
            sum(c.isdigit() for c in random_password) > 2
            and sum(c.isupper() for c in random_password) < 5
        ):
            break
    return random_password


if __name__ == "__main__":
    create_password()
