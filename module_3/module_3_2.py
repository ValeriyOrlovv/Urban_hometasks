def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' not in recipient or not any(
        [recipient.endswith('.com'),recipient.endswith('.ru'), recipient.endswith('.net')]
    ):
        return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    if sender == recipient:
        return 'Нельзя отправить письмо самому себе!'
    if sender == 'university.help@gmail.com':
        return f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.'
    if sender != 'university.help@gmail.com':
        return f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}'

print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))
