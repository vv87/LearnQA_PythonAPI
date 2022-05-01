from json.decoder import JSONDecodeError
from simplejson.scanner import JSONDecodeError
import requests

# 1
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# response = requests.get("https://playground.learnqa.ru/api/hello")
# print(response.text)


# 2
# payload = {"name": "User"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)
#
#
# payload = {"name": "User"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)


# 3
# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])

# 4
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])


# 5
# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except JSONDecodeError:
#     print("Response is not a JSON format")


# 6
# response = requests.put("https://playground.learnqa.ru/api/check_type")
# print(response.text)

# response = requests.get("https://playground.learnqa.ru/api/check_type", params={"param1": "value1"})
# print(response.text)
#
# response = requests.post("https://playground.learnqa.ru/api/check_type", data={"param1": "value1"})
# print(response.text)


# 7
# response = requests.post("https://playground.learnqa.ru/api/check_type")
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/something")
# print(response.status_code)
# print(response.text)


# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# print(response.status_code)

# response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# first_response = response.history[0]
# second_response = response
#
# print(first_response.url)
# print(second_response.url)


# 8
# headers = {"some_header": "123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers)
#
# # response header
# print(response.text)
# # request header
# print(response.headers)


# 9
# payload = {"login": "secret_login", "password": "secret_pass"}
# response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
#
# print(response.text)
# print(response.status_code)
# print(dict(response.cookies))


# payload = {"login": "secret_login", "password": "secret_pass2"}
# response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
#
# print(response.text)
# print(response.status_code)
# print(dict(response.cookies))


# payload = {"login": "secret_login", "password": "secret_pass"}
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
#
# cookie_value = response1.cookies.get('auth_cookie')
# cookies = {'auth_cookie': cookie_value}
# response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
# print(response2.text)


# payload = {"login": "secret_login", "password": "secret_pass"}
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
#
# cookie_value = response1.cookies.get('auth_cookie')
#
# cookies = {}
#
# if cookie_value is not None:
#     cookies.update({'auth_cookie': cookie_value})
#
# response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
# print(response2.text)


# payload = {"login": "secret_login", "password": "secret_pass2"}
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
#
# cookie_value = response1.cookies.get('auth_cookie')
#
# cookies = {}
#
# if cookie_value is not None:
#     cookies.update({'auth_cookie': cookie_value})
#
# response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
# print(response2.text)
