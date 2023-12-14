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
# players = read["PlayerID"].dropna().tolist()
players = [182877,335721,230784,392765,776890,282823,357164]

player_id_list = []
name_in_country_list = []
date_of_birth_list = []
place_of_birth_list = []
height_list = []
citizenship_list = []
position_list = []
foot_list = []
current_club_list = []
current_market_value_list = []

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux ×86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
for player in players:
    page =  f"https://www.transfermarkt.com/erling-haaland/profil/spieler/{int(player)}"
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree. content, 'html.parser')
    result = f.GetPlayerProfile(int(player), pageSoup)

    player_id_list += result[0]
    name_in_country_list += result[1]
    date_of_birth_list += result[2]
    place_of_birth_list += result[3]
    height_list += result[4]
    citizenship_list+= result[5]
    foot_list += result[6]
    current_club_list += result[7]
    current_market_value_list += result[8] # Has to be added in Functions.py
    
df = pd.DataFrame({"PlayerID": player_id_list, "Name in Country": name_in_country_list, "Date of Birth": date_of_birth_list, "Place of Birth": place_of_birth_list, "Height": height_list, "Citizenship": citizenship_list, "Foot": foot_list, "Current Club": current_club_list, "Current Market Value": current_market_value_list})
df.to_csv("player_profile.csv")  
print(df)

elapsed_time = stopwatch.stop()