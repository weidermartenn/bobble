import unittest
import json
from bottle import response
from utils import check_email
from myform import my_form

class TestApp(unittest.TestCase):
    # ���� ���������� ����
    def test_check_email_valid(self):
        self.assertTrue(check_email('example@gmail.com'))
        self.assertTrue(check_email('user_name@mail.ru'))

    # ���� ������������ ����
    def test_check_email_invalid(self):
        self.assertFalse(check_email('invalid_email'))
        self.assertFalse(check_email('example@example'))

if __name__ == '__main__':
    unittest.main()