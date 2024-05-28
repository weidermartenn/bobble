import re

def check_email(email):
    # Шаблон почты
    pattern = r"[a-zA-Z0-9]{1}[a-zA-Z0-9._\-]{4,29}[a-zA-Z0-9]{1}@(mail.ru|gmail.com|yandex.ru|inbox.ru|list.ru|bk.ru|internet.ru){1}$"
    # Проверка на соответствие шаблону
    if re.match(pattern, email):
        return True
    return False