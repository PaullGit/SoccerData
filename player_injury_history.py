# Make sure that 
# * sudo pip3 install requests
# * sudo pip3 install bs4 
# * sudo pip3 install pandas
# 
# were ran before executing the code beneath

import requests
from bs4 import BeautifulSoup
import pandas as pd
import functions as f
import stopwatch as sw
stopwatch = sw.Stopwatch()
stopwatch.start()

# Takes a CSV from all players
read = pd.read_csv("all_players.csv")
players = read["PlayerID"].dropna().tolist()
# first200 = players[:200]
# print(first200)

player_id_list = []
season_list = []
from_list = []
until_list = []
injury_list = []
days_list = []
games_missed_list = []

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux ×86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
for player in players:
    page =  f"https://www.transfermarkt.com/erling-haaland/verletzungen/spieler/{int(player)}"
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree. content, 'html.parser')
    result = f.GetPlayerInjuryHistory(int(player), pageSoup)
    player_id_list += result[0]
    season_list += result[1]
    injury_list += result[2]
    from_list += result[3]
    until_list += result[4]
    days_list += result[5]
    games_missed_list += result[6]

df = pd.DataFrame({"PlayerID": player_id_list, "Season": season_list, "Injury": injury_list, "From": from_list, "Until": until_list, "Days": days_list, "Games Missed": games_missed_list})
df.to_csv("player_injury_history.csv")  
print(df)

elapsed_time = stopwatch.stop()