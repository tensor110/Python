# Requests Module 

# The requests module allows you to send HTTP requests in Python, which is useful for interacting with web APIs or web scraping.

import requests
from bs4 import BeautifulSoup
# Get Request 
response = requests.get("https://www.google.com")
# print(response.text)

# To get the code in identation format we use bs4 module
res = BeautifulSoup(response.text, 'html.parser')
# print(res.prettify())

# To find all 'div' tag contents
for heading in res.find_all('div'):
    # print(heading.text)

# Post Request 
url = "https://jsonplaceholder.typicode.com/posts"
data={
    "title": "Post request",
    "body": "Request",
    "userId": 12
}
headers = {
    'Content-type': 'application/json; charset=UTF-8'
}
respo = requests.post(url, headers= headers, json= data)
print(respo.text)