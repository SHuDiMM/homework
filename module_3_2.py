def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if sender.find('@') == -1 or recipient.find('@') == -1:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")

    a = ['.com', '.net', '.ru']
    b = [recipient, sender]
    is_contains = 0
    for i in b:
        for j in a:
            if i.find(j) == len(i) - len(j):
                is_contains += 1
            else:
                continue

    if is_contains < 2:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')

    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')

send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')

send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
