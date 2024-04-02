from bottle import post, request

@post('/home')
def my_form():
    # Получаем данные из формы
    name = request.forms.get('NAME')    # Получаем имя
    mail = request.forms.get('ADRESS')  # Получаем адрес электронной почты
    date_str = request.forms.get('DATE')    # Получаем дату в виде строки
    return "Thanks %s! The answer will be sent to the email %s Access Date: %s" % (name, mail, date_str)
    
    
