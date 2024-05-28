from bottle import post, request
import json
from utils import check_email

@post('/home')
def my_form():
    quest = request.forms.get('QUEST')
    name = request.forms.get('NAME')  
    mail = request.forms.get('ADRESS') 
    date_str = request.forms.get('DATE')   
    
    # �������� �� ������������ ������ � ���� �������
    if len(quest) <= 3 or quest.isdigit():
        return "Please enter a valid question (more than 3 characters and not just digits)."
    
    # �������� �� ������������ ������ � ���� ����� ������������
    if not check_email(mail):
        return "Please enter a valid email address."
    
    # �������� ����� ������ � ������� �������, ������� ��� ����
    new_entry = {
        'NAME': name,
        'ADRESS': mail,
        'DATE': date_str,
        'QUESTIONS': []
    }
    
    try:
        # �������� ����� JSON ��� ������
        with open('data.json', 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                # ���� ���� ������ ��� �� �������� ��������� JSON, ������� ������ �������
                data = {}
    except FileNotFoundError:
        # ���� ���� �� ����������, ������� ������ �������
        data = {}
    
    # ���������� ����� ������ ��� ���������� ������������
    if mail in data:
        if quest not in data[mail]['QUESTIONS']:  # �������� �� ���������
            data[mail]['QUESTIONS'].append(quest)
    else:
        data[mail] = new_entry
        data[mail]['QUESTIONS'].append(quest)
    
    # ������ ������ � ���� JSON
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    return "Thanks, %s! The answer will be sent to the email %s. Access Date: %s" % (name, mail, date_str)