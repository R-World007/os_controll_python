import requests as req
resp = req.get("http://www.bbc.com")
print(resp.text)
