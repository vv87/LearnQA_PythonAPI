import requests


response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

print(response)
print(response.history)
print(response.url)
