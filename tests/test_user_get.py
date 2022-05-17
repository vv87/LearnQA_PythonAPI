from LearnQA_PythonAPI.lib.base_case import BaseCase
from LearnQA_PythonAPI.lib.assertions import Assertions
from LearnQA_PythonAPI.lib.my_requests import MyRequests
import allure


@allure.epic("User get request cases")
class TestUserGet(BaseCase):

    @allure.description("Get details of unauthorized user")
    def test_get_user_details_not_auth(self):
        response = MyRequests.get("/user/2")

        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    @allure.description("Get details of authorized user")
    def test_get_details_auth_as_same_user(self):

        data = {
            "email": "vinkotov@example.com",
            "password": "1234"

        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        expected_fields = ["username", "email", "firstName", "lastName"]

        Assertions.assert_json_has_keys(response2, expected_fields)

    @allure.description("Get details of authorized as another user")
    def test_get_details_auth_as_another_user(self):

        data = {
            "email": "vinkotov@example.com",
            "password": "1234"

        }

        response1 = MyRequests.post("/user/login", data=data)

        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")

        response2 = MyRequests.get(
            f"/user/544",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_json_has_key(response2, "username")

        not_expected_fields = ["email", "firstName", "lastName"]
        Assertions.assert_json_has_not_keys(response2, not_expected_fields)
