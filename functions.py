import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def GetPlayerName(club_id, pageSoup):
    html_names = pageSoup.find_all("img", {"class": "bilderrahmen-fixed lazy lazy"})
    list_names = [element['alt'] for element in html_names] 
    return list_names

def GetPlayerID(club_id, PageSoup):
    html_ids = pageSoup.find_all("td", {"class": "rechts hauptlink"})
    list_ids = []
    
    for element in html_ids:
        html_id= str(element)
        parts = html_id.split("/")	
        player_id = parts[4].split(">")[0]
        cleaned_player_id = ''.join(char for char in player_id if char.isdigit())
        list_ids.append(cleaned_player_id)
    list_club_ids = [club_id for i in range(0, len(list_ids))]
    return list_ids, list_club_ids

Names = []
IDs = []
ClubIDs = []
club_ids_premierleague = [985, 11, 281,631,31]
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux ×86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
for club_id in club_ids_premierleague:
    page =  f"https://www.transfermarkt.co.uk/clubname/startseite/verein/{club_id}"
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree. content, 'html.parser')
    Names += GetPlayerName(club_id, pageSoup)
    IDs += GetPlayerID(club_id, pageSoup)[0]
    ClubIDs += GetPlayerID(club_id, pageSoup)[1]


df = pd.DataFrame({"IDs": IDs, "Names": Names, "ClubIDs": ClubIDs })
df.to_csv("player_ids.csv", index=False)
print(df)