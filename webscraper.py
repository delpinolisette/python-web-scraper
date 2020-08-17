from bs4 import BeautifulSoup
import requests
import json

# url and response
url = "https://en.wikipedia.org/wiki/Cuba"
response = requests.get(url, timeout = 5)
#import code; code.interact(local=dict(globals(), **locals()))
content = BeautifulSoup(response.content, "html.parser")
# print(content)

# use selectors from bs4

# finds all paragraph tags on site, 
# can also add attributes
select_p = content.find_all('p')
#print(select_p)
x = 0

# loop over all such p elements
for select_p in content.find_all('p'):
	print(x)
	x= x + 1

# store data as JSON to make it easier to parse later
p_array = []

