import unittest
import json
from bottle import response
from utils import check_email
from myform import my_form

class TestApp(unittest.TestCase):
    def test_check_email_valid_default(self):
        self.assertTrue(check_email('example@gmail.com'))
        self.assertTrue(check_email('username@mail.ru'))
    
    def test_check_email_valid_underline(self):
        self.assertTrue(check_email('exa_mple@gmail.com'))
        self.assertTrue(check_email('U_ser_name@gmail.com'))
    
    def test_check_email_valid_with_digits(self):
        self.assertTrue(check_email('example123@gmail.com'))
        self.assertTrue(check_email('User_123name@gmail.com'))

    def test_check_email_invalid_default(self):
        self.assertFalse(check_email('invalid_email'))
        self.assertFalse(check_email('example@example'))
    
    def test_check_email_valid_symbols(self):
        self.assertFalse(check_email('?????@gmail.com'))
        self.assertFalse(check_email('!%%@gmail.com'))

if __name__ == '__main__':
    unittest.main()