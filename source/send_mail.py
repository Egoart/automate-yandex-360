import smtplib
import logging

from email.message import EmailMessage
from utils import FROM_EMAIL as from_email
from utils import SENDER_EMAIL_PASSWORD as password


def send_mail_to_initiator(user_data, api_user_data):
    to_email = user_data["initiator_email"]
    # Set up the SMTP server
    try:
        with smtplib.SMTP("smtp.yandex.ru", 587) as s:
            s.starttls()
            s.login(from_email, password)

            subject = "Подтверждение создания адреса электронной почты"

            msg = (
                f"Здравствуйте!\n\n"
                f"По вашему запросу создан адрес электронной почты для пользователя:\n\n"
                f"{api_user_data['last_name']} {api_user_data['first_name']} {api_user_data['middle_name']}\n\n"
                f"Логин: {api_user_data['email']}\n"
                f"Временный пароль: {api_user_data['password']}\n\n"
                f"ВНИМАНИЕ! Пароль необходимо сменить на свой персональный. Для этого, после входа в почтовый ящик, расположенный на Яндексе, нажать на изображение шестеренки, расположенное вверху справа в основном окне почты (там где список писем), далее перейти по ссылке 'Все настройки', далее перейти по ссылке 'Безопасность', далее перейти по ссылке 'менять пароль'.\n\n\n"
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

    except smtplib.SMTPException as err:
        logging.error("Сообщение не было отправлено", err)
