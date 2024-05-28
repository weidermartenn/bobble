import unittest
import json
from bottle import response
from utils import check_email
from myform import my_form

class TestApp(unittest.TestCase):
    def test_check_email(self):
        self.assertTrue(check_email('example@gmail.com'))
        self.assertTrue(check_email('user_name@mail.ru'))
        self.assertFalse(check_email('invalid_email'))
        self.assertFalse(check_email('example@example'))

    def test_my_form(self):
        # Test for valid input
        with self.subTest(msg='Valid input'):
            with open('data.json', 'w') as file:
                json.dump({}, file)
            response.body = my_form()
            self.assertIn('Thanks', response.body)
            with open('data.json', 'r') as file:
                data = json.load(file)
            self.assertIn('example@gmail.com', data)
            self.assertIn('QUESTIONS', data['example@gmail.com'])
            self.assertIn('test question', data['example@gmail.com']['QUESTIONS'])

        # Test for empty question
        with self.subTest(msg='Empty question'):
            with open('data.json', 'w') as file:
                json.dump({}, file)
            response.body = my_form()
            self.assertIn('Please enter a valid question', response.body)

        # Test for invalid email
        with self.subTest(msg='Invalid email'):
            with open('data.json', 'w') as file:
                json.dump({}, file)
            response.body = my_form()
            self.assertIn('Please enter a valid email address', response.body)

if __name__ == '__main__':
    unittest.main()