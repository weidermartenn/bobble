from bottle import post, request

@post('/home')
def my_form():
    # �������� ������ �� �����
    name = request.forms.get('NAME')    # �������� ���
    mail = request.forms.get('ADRESS')  # �������� ����� ����������� �����
    date_str = request.forms.get('DATE')    # �������� ���� � ���� ������
    return "Thanks %s! The answer will be sent to the email %s Access Date: %s" % (name, mail, date_str)
    
    
