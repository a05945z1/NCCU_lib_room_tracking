
from bs4 import BeautifulSoup
import requests
import re


url = 'http://rbs.lib.nccu.edu.tw:8080/nccuroom/co/studyroom.jsp'
resp = requests.get(url)
#print(resp.status_code)


soup = BeautifulSoup(resp.text, 'html.parser')


unav_lst=[]
all_lst=[]
unav_rooms = soup.find_all("div",re.compile("inuse disabled"))
rooms = soup.find_all("div",re.compile("num"))
for index,room in enumerate(rooms[:]):
    if room.string!=None:
        all_lst.append(room.string)
for index,unav_room in enumerate(unav_rooms[:]):
    m = re.search(r'(?<=\n)\w+',unav_room.text)
    unav_lst.append(m.group(0))


if len(unav_lst)==len(all_lst):
    print("no seat available")
else:
    print("seats available:",len(all_lst)-len(unav_lst))

