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
# players = [182877,335721,230784,392765,776890,282823,357164]
players = [418560]
player_id_list = []
player_club_list= []
date_of_birth_list = []
place_of_birth_list = []
citizenship_list = []
height_list = []

current_market_value_list = [] #TBD

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux ×86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
for player in players:
    page =  f"https://www.transfermarkt.com/erling-haaland/profil/spieler/{int(player)}"
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree. content, 'html.parser')
    result = f.GetPlayerProfile(int(player), pageSoup)
    # print(result)
    player_id_list += result[0]
    player_club_list += result[1]
    date_of_birth_list += result[2]
    place_of_birth_list += result[3]
    height_list += result[4]
    citizenship_list+= result[5]
    current_market_value_list += result[6] # Has to be added in Functions.py
    
    print(player_id_list)
    print(player_club_list) 
    print(date_of_birth_list)
    print(place_of_birth_list)
    print(height_list)
    print(citizenship_list)
    print(current_market_value_list)
# df = pd.DataFrame({"PlayerID":player_id_list, "Club":player_club_list, "DateOfBirth":date_of_birth_list, "PlaceOfBirth":place_of_birth_list, "Height":height_list, "Citizenship":citizenship_list, "CurrentMarketValue":current_market_value_list})
# df.to_csv("player_profile.csv") 
# print(df)

elapsed_time = stopwatch.stop()