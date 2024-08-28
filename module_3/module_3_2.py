def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if (
        ('@' not in sender or '@' not in recipient) or
        ('.ru' not in sender or 'ru' not in recipient) or
        ('.net' not in sender or '.net' not in recipient) or
        ('.com' not in sender or '.com' not in recipient)
    ):
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}".')
    if sender != 'university.help@gmail.com':
        return print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')
    if sender == recipient:
        return print('Нельзя отправить письмо самому себе!')
    return print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
