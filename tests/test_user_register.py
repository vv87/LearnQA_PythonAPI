from datetime import datetime
import requests
import pytest
from LearnQA_PythonAPI.lib.base_case import BaseCase
from LearnQA_PythonAPI.lib.assertions import Assertions


class TestUserRegister(BaseCase):

    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vincotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user", data=data)

        Assertions.assert_code_status(response, 400)
        Assertions.assert_response_content_equal_actual_result(
            response,
            f"Users with email '{email}' already exists",
            f"Unexpected response content {response.content}"
        )

    def test_create_user_with_incorrect_email(self):
        email = 'asfvexample.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/api/user", data=data)

        Assertions.assert_response_content_equal_actual_result(
            response,
            f"Invalid email format",
            f"Response content not equal 'Invalid email format'"
        )
        Assertions.assert_code_status(response, 400)

    def test_create_user_with_short_name(self):
        data = {
            'password': '123',
            'username': '1',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user", data=data)

        Assertions.assert_response_content_equal_actual_result(
            response,
            f"The value of 'username' field is too short",
            f"There is no \"The value of 'username' field is too short\" text in response content"
        )
        Assertions.assert_code_status(response, 400)

    def test_create_user_with_long_name(self):
        data = {
            'password': '123',
            'username': "1" * 251,
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/api/user", data=data)

        Assertions.assert_response_content_equal_actual_result(
            response,
            f"The value of 'username' field is too long",
            f"There is no \"The value of 'username' field is too long\" text in response content, if name >250 symbols"
        )
        Assertions.assert_code_status(response, 400)

    email = datetime.now().strftime("%m%d%Y%H%M%S") + "@example.com"
    assert_value_first_part = "The following required params are missed: "

    data_without_pass = {
        'username': "learnqa",
        'firstName': 'learnqa',
        'lastName': 'learnqa',
        'email': email
    }

    expected1 = assert_value_first_part + "password"

    data_without_username = {
        'password': '123',
        'firstName': 'learnqa',
        'lastName': 'learnqa',
        'email': email
    }

    expected2 = assert_value_first_part + "username"

    data_without_firstname = {
        'password': '123',
        'username': "learnqa",
        'lastName': 'learnqa',
        'email': email
    }

    expected3 = assert_value_first_part + "firstName"

    data_without_lastname = {
        'password': '123',
        'username': "learnqa",
        'firstName': 'learnqa',
        'email': email
    }

    expected4 = assert_value_first_part + "lastName"

    data_without_email = {
        'password': '123',
        'username': "learnqa",
        'firstName': 'learnqa',
        'lastName': 'learnqa'
    }

    expected5 = assert_value_first_part + "email"

    @pytest.mark.parametrize('data, expected', [(data_without_pass, expected1),
                                                (data_without_username, expected2),
                                                (data_without_firstname, expected3),
                                                (data_without_lastname, expected4),
                                                (data_without_email, expected5)])
    def test_create_user_without_one_of_fields(self, data, expected):
        response = requests.post("https://playground.learnqa.ru/api/user", data=data)

        Assertions.assert_response_content_equal_actual_result(
            response,
            expected,
            f"There is no '{expected}' text in response content, current text is: " + response.content.decode("utf-8")
        )
        Assertions.assert_code_status(response, 400)
