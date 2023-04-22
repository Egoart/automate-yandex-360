# About
This project is intended to automate email creation, updating and recording user's profiles on Yandex 360 platform.

Profiles are created based on user's personal info obtained either via manual data entry or from Excel file contained strucutred user's data. Emails can be genereated in two ways: manualy (arbitrary email name) and automatically (based on user first and last names using transliteration from сyrillic to latin). Upon new profile creation the list of all excisting profiles is generated and placed in separate Excel file. Password is generated automatically. The person who is initiated profile creation recieves an email message containing login and password for a new profile.

# How to use

## Initial setup

1. Install Python and packages from requirements.txt. Python version 3.9.2.
2. Create `.env` file in the root directory of the project. Add to this file:
   - `BASE_URL=https://api360.yandex.net/directory/v1/org/` (base URL for script's use cases, [see for reference](https://yandex.ru/dev/api360/doc/ref/index.html))
   - `COMPANY_ID` (Company ID obtained from yandex. To get ID [authorize on Yandex](https://passport.yandex.ru/) and [register your application](https://yandex.ru/dev/api360/doc/concepts/access.html))
   - `TOKEN` (OAUTH secret token obtained from Yandex for your Y360 account. [About token - Yandex](https://yandex.ru/dev/id/doc/ru/concepts/ya-oauth-intro))
   - `EMAIL` (sender email from which massage with confirmation of new email registration is sent)[^1]
   - `SENDER_EMAIL_PASSWORD` (password to `EMAIL` mailbox)[^1]
3. If you'd like to create users from Excel file template, fill this file with correct data, named it `email_form_v1.1.xlsx` and place in the project's folder `source`. The structure of the file as following: "initiator_email" in "B1" cell, last_name - "A4","first_name" - "B4", "middle_name" - "C4", "position" - "D4", "phone" - "E4", "department name" - "F4". In "F4" the dropdown with department names are located. The source of names are on separate Excel sheet.

## Create new user's email on Y360

1. Run `main.py` from `source` folder
2. Fill in the input prompts[^2]. 
3. Check the response from Y360 API[^3]

By running main script you also run additional scripts. One of them generates actual list of all users containing a new one as well and another sends email via SMTP which confirms creation of new user and contains its credentials[^4]. 

You have two options how to generate email: eneter arbitrary email login or let the script generate it authomatically. The authomatic email generation is based on user's first and last names and results in email like first letter of user name followed by dot followed by transliterated full user's last name and finaly followed by @ and domain name. Transliteration is made based on [Western Unuon transliteration table](https://www.westernunion.ru/ru/en/transliteration-table.html).

## Add/edit phone number for existing user

If you'd like to add or update phone number in existing user's contact info, run `update_users.py` from `source` folder and fill in input prompts. You'll be asked for user's valid email and new phone number. With this option you may update info for one or many users.

## Get/update list of all contacts on your domain from Y360
You may get list of all contacts without adding new user just by running `create_users_list.py` from `source` folder. As a result Excel file `emails_list.xlsx` will be generated. To update this file run again `create_users_list.py`. It is not necessary to delete Excel file previously created[^5].

## Generate password
To generate temporarily password run `create_password.py`. Password will be printed out in a terminal.

# TO DO

* Change hardcoded department numbers in `handle_dept_input` function in `validations.py`
* Parse data for multiple user from `email_form_v1.1.xlsx` file
* Correct PATH to Excel files to separate them from project files
* Timeouts for API requests
* Password expire time function
* Test signature settings API [ref](https://yandex.ru/dev/api360/doc/ref/MailUserSettingsService/MailUserSettingsService_SetSenderInfo.html)

[^1]: Do not forget to allow SMTP usage in your mailbox settings. In Yandex its is checkbox for IMAP for some unknown reasons.
[^2]: New user is created with `"timezone": "Europe/Minsk"`, to cvhange this edit `request_body` variable in `create_user` function in `add_new_user.py`.
[^3]: Do not forget to change the text of the email confirmation message and signature in `send_message.py` variable `msg`.
[^4]: Note that phone number is validated against `+375` phone code and `XX XXX XX XX` phone format. To change this, edit `check_phone_number` and `format_phone_number` in `validations.py`.
[^5]: Please note that list in `emails_list.xlsx` do not contain some service emails and administrator email as they are intentionally cut off. To change number of listed emails, edit slicing argument in declaration of users_list_excl_service_emails variable in `create_users_list.py`.
