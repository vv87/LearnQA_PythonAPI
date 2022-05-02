import time
import requests


url = "https://playground.learnqa.ru/ajax/api/longtime_job"


# 1. скрипт, который создает задачу
response_1 = requests.get(url).json()

# parse secs from response
seconds = response_1['seconds']
# print(response_1, seconds)

# 2. скрипт, который делает один запрос с token ДО того, как задача готова и убеждается в правильности поля status
response_json = response_1
response_2 = requests.get(url, params=response_json).json()
assert response_2["status"] == 'Job is NOT ready'

# print(response_2.json())
# print(response_json["token"])
# print(response_2["status"])

# 3. скрипт, который ждет нужное количество секунд
# 4. скрипт, который делал бы один запрос c token ПОСЛЕ того, как задача готова,
# убеждался в правильности поля status и наличии поля result
time.sleep(seconds)
response_json = response_1
response_3 = requests.get(url, params=response_json).json()
assert response_3["status"] == 'Job is ready'
assert "result" in response_3
