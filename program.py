# Make sure that 
# * sudo pip3 install requests
# * sudo pip3 install bs4 
# * sudo pip3 install pandas

# were ran before executing the code beneath


import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def GetPlayerNameID(club_id):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux ×86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    page =  f"https://www.transfermarkt.co.uk/clubname/startseite/verein/{club_id}"
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree. content, 'html.parser')
    #Get club id
    club_id = page.split("/")[-1]


    Names = pageSoup.find_all("img", {"class": "bilderrahmen-fixed lazy lazy"})
    IDs =  pageSoup.find_all("td", {"class": "rechts hauptlink"})

    #Seeding Data
    NamesList = [element['alt'] for element in Names] 
    NamesList = NamesList
    for i in range(0, len(NamesList)):
        html_string = str(IDs[i])
        match = re.search(r'/spieler/(\d+)', html_string)
        if match:
            player_id = match.group(1)
            IDsList.append(player_id)
        else:
            IDsList.append("NULL")

    for i in range(0, len(Names)):
        ClubIDsList.append(club_id)

    print(NamesList)
    print("COUNT OF " + str(len(NamesList)) + " NAMES")
    print(IDsList)
    print("COUNT OF " + str(len(IDsList)) + " IDS")
    return NamesList, IDsList, ClubIDsList

NamesList = []
IDsList = []
ClubIDsList = []
club_ids_premierleague = [985, 11, 281,631,31]
for club_id in club_ids_premierleague:
    NamesList += GetPlayerNameID(club_id)[0]    
    IDsList += GetPlayerNameID(club_id)[1]
    ClubIDsList += GetPlayerNameID(club_id)[2]
# print(NamesList)
# print(len(NamesList))
# print(IDsList)
# print(len(IDsList))

