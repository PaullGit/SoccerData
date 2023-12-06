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
ligue_1 = [583, 162, 273, 244, 417, 1082, 826, 1041,667, 995, 1421, 1158, 969,415, 3911,738, 3524, 347]
la_liga = [418, 131, 13, 681, 621,150, 368, 1050, 1049, 12321, 940,331,3709,3302, 237, 367, 16795, 2687, 472,1108]
bundesliga = [27, 15, 23826, 16, 82, 18, 89, 24, 79, 60, 533, 167, 39, 3, 86, 80, 2036, 105]
brasileiro = [614,1023,585,679,199,300, 2462, 6600, 221, 8793, 978,537, 10010, 210, 609, 776, 10870, 2863, 3197, 28022]

leagues = [premier_league, series_a, eredivisie, ligue_1, la_liga, bundesliga]
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

df = pd.DataFrame({"IDs": IDs, "Names": Names, "ClubIDs": ClubIDs })

print(df)