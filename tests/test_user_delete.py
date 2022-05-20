import allure
from ..lib.base_case import BaseCase
from ..lib.assertions import Assertions
from ..lib.my_requests import MyRequests


@allure.epic("User delete request cases")
class TestUserDelete(BaseCase):

    @allure.description("Unable to delete user with ID 2")
    def test_delete_user_by_id2(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        print(response1.content)
        print(response1.cookies)
        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get("/user/auth",
                                   headers={"x-csrf-token": self.token},
                                   cookies={"auth_sid": self.auth_sid}
                                   )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "User id from auth method is not equal to user id from check method"
        )

        # DELETE
        response3 = MyRequests.delete("/user/2",
                                      data=data,
                                      headers={"x-csrf-token": self.token},
                                      cookies={"auth_sid": self.auth_sid}
                                      )
        expected = "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

        Assertions.assert_code_status(response3, 400)

        Assertions.assert_response_content_equal_actual_result(
            response3,
            expected,
            f"There is no '{expected}' text in response content, current text is: " + response3.content.decode("utf-8")
        )

    @allure.description("Create a user, log in from under him, delete, then try to get his data by ID "
                        "and make sure that the user is really deleted.")
    def test_create_and_delete_user_by_id(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        self.email = register_data['email']
        self.first_name = register_data['firstName']
        self.password = register_data['password']
        self.user_id = self.get_json_value(response1, 'id')

        # LOGIN
        login_data = {
            'email': self.email,
            'password': self.password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        self.auth_sid = self.get_cookie(response2, "auth_sid")
        self.token = self.get_header(response2, "x-csrf-token")

        # DELETE
        response3 = MyRequests.delete("/user/2",
                                      data=login_data,
                                      headers={"x-csrf-token": self.token},
                                      cookies={"auth_sid": self.auth_sid}
                                      )

        Assertions.assert_code_status(response3, 200)

        # GET
        expected = "User not found"

        response4 = MyRequests.get(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
        )

        print(response4.content)
        Assertions.assert_code_status(response3, 200)
        Assertions.assert_response_content_equal_actual_result(
            response4,
            expected,
            f"There is no '{expected}' text in response content, current text is: " + response4.content.decode("utf-8")
        )

    @allure.description("Try to delete a user while being logged in by another user")
    def test_ry_to_delete_another_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        self.email = register_data['email']
        self.first_name = register_data['firstName']
        self.password = register_data['password']
        self.user_id = self.get_json_value(response1, 'id')

        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        self.auth_sid = self.get_cookie(response2, "auth_sid")
        self.token = self.get_header(response2, "x-csrf-token")

        # DELETE
        data = {
            'email': self.email,
            'password': self.password
        }
        response3 = MyRequests.delete("/user/2",
                                      data=data,
                                      headers={"x-csrf-token": self.token},
                                      cookies={"auth_sid": self.auth_sid}
                                      )

        expected = "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

        Assertions.assert_code_status(response3, 400)

        Assertions.assert_response_content_equal_actual_result(
            response3,
            expected,
            f"There is no '{expected}' text in response content, current text is: " + response3.content.decode("utf-8")
        )
