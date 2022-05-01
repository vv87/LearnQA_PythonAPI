import requests


response = requests.post("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

print(response.history)

first_response = response.history[0]
second_response = response.history[1]

print(first_response.url)
print(second_response.url)

# result:
# [<Response [301]>, <Response [301]>]
# https://playground.learnqa.ru/api/long_redirect
# https://playground.learnqa.ru/
