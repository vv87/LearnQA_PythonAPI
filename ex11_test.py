import requests


def test_cookie():
    url_homework_cookie = requests.get("https://playground.learnqa.ru/api/homework_cookie").cookies
    homework_cookie = "HomeWork"
    hw_value = "hw_value"
    check_homework_value = url_homework_cookie[homework_cookie]
    print(check_homework_value)

    assert hw_value in check_homework_value, f'There is no {hw_value} in {homework_cookie} cookie'
