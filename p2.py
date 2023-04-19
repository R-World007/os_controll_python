import requests
url=requests.head("http://google.com")
print(url.headers)
