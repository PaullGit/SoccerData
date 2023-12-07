import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import functions as f
import leagues as l
import stopwatch as sw

stopwatch = sw.Stopwatch()
stopwatch.start()
Names = []
IDs = []
ClubIDs = []

leagues = [l.premier_league, l.series_a, l.eredivisie, l.ligue_1, l.la_liga, l.bundesliga, l.brasileiro]
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux ×86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
for league in leagues:
    for club_id in league:
        page =  f"https://www.transfermarkt.co.uk/clubname/startseite/verein/{club_id}"
        pageTree = requests.get(page, headers=headers)
        pageSoup = BeautifulSoup(pageTree. content, 'html.parser')
        name_id_club = f.GetPlayers(club_id, pageSoup)
        IDs += name_id_club[0]
        Names += name_id_club[1]
        ClubIDs += name_id_club[2]

df = pd.DataFrame({"PlayerID": IDs, "PlayerName": Names, "ClubID": ClubIDs })
df.to_csv("all_players.csv")
print(df)
elapsed_time = stopwatch.stop()