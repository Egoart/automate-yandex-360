import smtplib
import logging

from email.message import EmailMessage
from utils import FROM_EMAIL as from_email

# from utils import SENDER_EMAIL_PASSWORD as password
from utils import YANDEX_APP_PASSWORD as password


def send_test_mail():
    to_email = "tech@belagrogen.by"
    # Set up the SMTP server
    try:
        with smtplib.SMTP("smtp.yandex.ru", 587) as s:
            s.starttls()
            s.login(from_email, password)

            subject = "Тестовое письмо"

            msg = (
                f"Здравствуйте!\n\n"
                f"Это тестовое письмо!\n\n"
                f"--\n"
                f"С уважением,\n"
                f"Егор Черявяковский\n"
                f"+375 44 510 37 44\n"
                f"ООО 'Научно-производственный центр БелАгроГен'\n"
                f"223053, Минский р-н,\n"
                f"пересечение Логойского тракта и МКАД,\n"
                f"административное здание, офис 411\n"
                f"https://www.belagrogen.by/\n\n"
            )

            em = EmailMessage()
            em["To"] = to_email
            em["From"] = from_email
            em["BCC"] = from_email
            em["Subject"] = subject
            em.set_content(msg)

            # Send the email
            s.send_message(em)
            print("Email was sent.")

    except smtplib.SMTPResponseException as err:
        # logging.error("Сообщение не было отправлено", err)
        error_code = err.smtp_code
        error_message = err.smtp_error
        print(f"{error_message} -- {error_code}")


if __name__ == "__main__":
    send_test_mail()
