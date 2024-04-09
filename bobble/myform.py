from bottle import post, request
import pdb

@post('/home')
def my_form():
    questions = {}
    quest = request.forms.get('QUEST')
    name = request.forms.get('NAME')  
    mail = request.forms.get('ADRESS') 
    date_str = request.forms.get('DATE')   
    
    questions.setdefault(mail, quest)
    pdb.set_trace()
    return("Thanks, %s! The answer will be sent to the email %s Access Date: %s" % (name, mail, date_str))
    
