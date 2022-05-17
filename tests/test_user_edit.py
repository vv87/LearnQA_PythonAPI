from LearnQA_PythonAPI.lib.base_case import BaseCase
from LearnQA_PythonAPI.lib.assertions import Assertions
from LearnQA_PythonAPI.lib.my_requests import MyRequests


class TestUserEdit(BaseCase):
    def register(self):
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        self.email = register_data['email']
        self.first_name = register_data['firstName']
        self.password = register_data['password']
        self.user_id = self.get_json_value(response1, 'id')

    def login(self):
        login_data = {
            'email': self.email,
            'password': self.password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        self.auth_sid = self.get_cookie(response2, "auth_sid")
        self.token = self.get_header(response2, "x-csrf-token")

    def edit(self):
        self.new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data={"firstName": self.new_name}
        )

        Assertions.assert_code_status(response3, 200)

    def get(self):
        self.response4 = MyRequests.get(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
        )

        Assertions.assert_json_value_by_name(
            self.response4,
            "firstName",
            self.new_name,
            "Wrong name of the user after edit"
        )

    def test_edit_just_created_user(self):
        self.register()
        self.login()
        self.edit()
        self.get()

    # Попытаемся изменить данные пользователя, будучи неавторизованными
    def test_edit_not_auth_user(self):
        self.register()

        # EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": 'token'},
            cookies={"auth_sid": 'auth_sid'},
            data={"firstName": new_name}
        )

        expected = "Auth token not supplied"

        Assertions.assert_code_status(response3, 400)

        Assertions.assert_response_content_equal_actual_result(
            response3,
            expected,
            f"There is no '{expected}' text in response content, current text is: " + response3.content.decode("utf-8")
        )

    # - Попытаемся изменить данные пользователя, будучи авторизованными другим пользователем
    def test_try_edit_user_being_authorized_by_another_user(self):
        self.register()
        self.login()

        # EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/2",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

    # - Попытаемся изменить email пользователя, будучи авторизованными тем же пользователем,
    # на новый email без символа @
    def test_edit_user_email_on_not_valid_email(self):
        self.register()
        self.login()

        # EDIT
        not_valid_email = "1234567890example.ru"
        expected = "Invalid email format"

        response4 = MyRequests.put(
            f"/user/2",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data={"email": not_valid_email}
        )

        Assertions.assert_code_status(response4, 400)

        Assertions.assert_response_content_equal_actual_result(
            response4,
            expected,
            f"There is no '{expected}' text in response content, current text is: " + response4.content.decode("utf-8")
        )

    # - Попытаемся изменить firstName пользователя, будучи авторизованными тем же пользователем,
    # на очень короткое значение в один символ
    def test_edit_auth_user_on_short_firstname(self):
        self.register()
        self.login()

        # EDIT
        new_name = "1"

        response3 = MyRequests.put(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": 'token'},
            cookies={"auth_sid": 'auth_sid'},
            data={"firstName": new_name}
        )

        expected = "Auth token not supplied"

        Assertions.assert_code_status(response3, 400)

        Assertions.assert_response_content_equal_actual_result(
            response3,
            expected,
            f"There is no '{expected}' text in response content, current text is: " + response3.content.decode("utf-8")
        )
