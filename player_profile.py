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

players = [182877,335721,230784,392765,776890,282823,357164]
player_id_list = [] #check
player_club_list = [] #check
player_name_list = [] #check
date_of_birth_list = [] #check
place_of_birth_list = [] #check
citizenship_list = [] #check
height_list = [] #check

position_list = [] #Not available
foot_list = [] #Not available

current_market_value_list = [] #check

for player in players: 
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux ×86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    page = f"https://www.transfermarkt.com/yan-couto/profil/spieler/{int(player)}"
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree. content, 'html.parser')
    result = f.GetPlayerProfile(player, pageSoup)

    player_id_list += result[0]
    player_club_list += result[1]
    player_name_list += result[2]
    date_of_birth_list += result[3]
    place_of_birth_list += result[4]
    citizenship_list += result[5]
    height_list += result[6]

print(player_id_list)
print(player_club_list)
print(player_name_list)
print(date_of_birth_list)
print(place_of_birth_list)
print(citizenship_list)
print(height_list)
df = pd.DataFrame({"PlayerID": player_id_list, "PlayerName": player_name_list, "Club": player_club_list, "DateOfBirth": date_of_birth_list, "PlaceOfBirth": place_of_birth_list, "Citizenship": citizenship_list, "Height": height_list})
df.to_csv("player_profile_testing.csv")
print(df)
elapsed_time = stopwatch.stop()