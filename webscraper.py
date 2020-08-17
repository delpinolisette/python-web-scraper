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
    print(select_p, "is p")
    x= x + 1

# store data as JSON to make it easier to parse later
p_array = []

for select_p in content.find_all('div'):
    # need to check its not NoneType
    # breakpoint()
    #import code; code.interact(local=dict(globals(), **locals()))
    # need to iterate through link and p elements!!!
    links = select_p.find_all('a')
    pgraphs = select_p.find_all('p')
    # stores all current links
    link_for_curr_p = []
    # stores all current paragraphs
    p_for_curr_p = []
    for link in links:
        #import code; code.interact(local=dict(globals(), **locals()))
        breakpoint()
        link_for_curr_p.append(link)
        # need to parse through link here!
    for p in pgraphs:
        p_for_curr_p.append(p)
    if (link_for_curr_p == []) | (p_for_curr_p == []):
        continue
    # breakpoint()
    curr_p = {
        "links": link_for_curr_p,
        "info": p_for_curr_p
    }
    # wipe array
    link_for_curr_p = []
    # wipe array
    p_for_curr_p = []
    # print(curr_p)
    p_array.append(curr_p)

with open('wikiData.json', 'w') as outfile:
    #breakpoint()
    # import code; code.interact(local=dict(globals(), **locals()))
    json.dump(p_array, outfile)