import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import functions as f

Names = []
IDs = []
ClubIDs = []

premier_league = [985, 11, 281,631,31,148, 762, 405, 379, 1237, 703, 1148, 873, 29, 989, 543, 931,1132, 350,1031]
series_a = [6195, 46, 5, 506, 12, 800, 398, 430,416, 1025, 6574, 410, 252, 2919, 380, 749, 276, 1005, 1390, 8970]
eredivisie = [234, 383, 610,1090,317,200,306,467,468,499,798,385,1435,1269,723,1304,724,235]
ligue_1 = []
la_liga = []
bundesliga = []

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux ×86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
for club_id in eredivisie:
    page =  f"https://www.transfermarkt.co.uk/clubname/startseite/verein/{club_id}"
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree. content, 'html.parser')
    Names += f.GetPlayerName(club_id, pageSoup)
    IDs += f.GetPlayerID(club_id, pageSoup)[0]
    ClubIDs += f.GetPlayerID(club_id, pageSoup)[1]
    print(str (f.Validate(Names, IDs)) + " " + str(club_id))


df = pd.DataFrame({"IDs": IDs, "Names": Names, "ClubIDs": ClubIDs })
print(df)