import requests


def test_header():
    url_homework_header = requests.get("https://playground.learnqa.ru/api/homework_header").headers
    home_work_header = "x-secret-homework-header"
    secret_value = "Some secret value"
    check_home_work_value = url_homework_header[home_work_header]
    # print(url_homework_header)

    assert secret_value in check_home_work_value, f'There is no {secret_value} in {home_work_header}'
