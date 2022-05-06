import requests


def test_cookie():
    url_homework_cookie = requests.get("https://playground.learnqa.ru/api/homework_cookie").cookies
    check_homework_value = url_homework_cookie["HomeWork"]
    print(check_homework_value)

    assert "hw_value" in check_homework_value, "f'There is no \"hw_value\" in \"HomeWork\" cookie'"
