import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

methods = ["GET", "POST", "PUT", "DELETE"]


'''
1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
'''

print(requests.get(url), requests.get(url).text)
# result:
# <Response [200]> Wrong method provided

print(requests.post(url), requests.post(url).text)
# <Response [200]> Wrong method provided

print(requests.put(url), requests.put(url).text)
# <Response [200]> Wrong method provided

print(requests.delete(url), requests.delete(url).text)
# <Response [200]> Wrong method provided


'''
2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
'''

print(requests.head(url), requests.head(url).text)
# <Response [400]>


'''
3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
   Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
   И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
   но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
'''

print('\n')

for method in methods:
    print(f'Response to a GET request with a {method} method in the parameter is:')
    param = {"method": method}
    response = requests.get(url, params=param)
    print(response.text)

    # result:
    # Response to a GET request with a GET method in the parameter is:
    #     {"success":"!"}
    # Response to a GET request with a POST method in the parameter is:
    #     Wrong method provided
    # Response to a GET request with a PUT method in the parameter is:
    #     Wrong method provided
    # Response to a GET request with a DELETE method in the parameter is:
    #     Wrong method provided

print('\n'*2)

for method in methods:
    print(f'Response to a POST request with a {method} method in the data is:')
    data = {"method": method}
    response = requests.post(url, data=data)
    print(response.text)

    # Response to a POST request with a GET method in the data is:
    # Wrong method provided
    # Response to a POST request with a POST method in the data is:
    #     {"success":"!"}
    # Response to a POST request with a PUT method in the data is:
    #     Wrong method provided
    # Response to a POST request with a DELETE method in the data is:
    #     Wrong method provided


print('\n'*2)

for method in methods:
    print(f'Response to a PUT request with a {method} method in the data is:')
    data = {"method": method}
    response = requests.put(url, data=data)
    print(response.text)

    # Response to a PUT request with a GET method in the data is:
    #     Wrong method provided
    # Response to a PUT request with a POST method in the data is:
    #     Wrong method provided
    # Response to a PUT request with a PUT method in the data is:
    #     {"success":"!"}
    # Response to a PUT request with a DELETE method in the data is:
    #     Wrong method provided


print('\n'*2)

for method in methods:
    print(f'Response to a DELETE request with a {method} method in the data is:')
    data = {"method": method}
    response = requests.delete(url, data=data)
    print(response.text)

    # Response to a DELETE request with a GET method in the data is:
    # {"success":"!"}
    # Response to a DELETE request with a POST method in the data is:
    #     Wrong method provided
    # Response to a DELETE request with a PUT method in the data is:
    #     Wrong method provided
    # Response to a DELETE request with a DELETE method in the data is:
    #     {"success":"!"}
