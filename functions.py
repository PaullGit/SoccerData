import re
from bs4 import BeautifulSoup

def validate(a ,b, club_id):
    if len(a) != len(b):
        print("a: " + str( len(a)) )
        print("b: " + str( len(b)) )
        print("False on club_id: " + str(club_id))

def clean_player_name(player_name):
    if len(player_name) == 0:
        return "NULL"
    input_string = player_name[0].get_text(strip=True)
    only_letters = re.sub(r'[0-9#]', '', input_string)
    find_capitals = re.sub(r'([A-Z])', r' \1', only_letters)
    cleaned_string = find_capitals.lstrip()
    return cleaned_string

def GetPlayers(club_id, pageSoup):
    #PAGE SOUPING
    html_names = pageSoup.find_all("img", {"class": "bilderrahmen-fixed lazy lazy"})
    list_names = [element['alt'] for element in html_names] 

    html_ids = pageSoup.find_all("td", {"class": "rechts hauptlink"})
    list_ids = []

    #SEEDING DATA
    for element in html_ids:
        html_id= str(element)
        parts = html_id.split("/")
        if len(parts) > 5:   
            player_id = parts[4].split(">")[0]
            cleaned_player_id = ''.join(char for char in player_id if char.isdigit())
        else: 
            cleaned_player_id = "NULL"
        list_ids.append(cleaned_player_id)
    list_club_ids = [club_id for i in range(0, len(list_ids))]
    validate(list_names, list_ids, club_id)
    
    return list_ids,list_names, list_club_ids

def GetPlayerInjuryHistory(player, pageSoup):
    #PAGE SOUPING
    SeasonFromUntil = pageSoup.find_all("td", {"class": "zentriert"})
    Injury = pageSoup.find_all("td", {"class": "hauptlink"})
    DaysGamesMissed = pageSoup.find_all("td", {"class": "rechts"})

    #SEEDING DATA
    player_id_list = []
    season_list = []
    from_list = []
    until_list = []
    injury_list = []
    days_list = []
    games_missed_list = []
    for _ in range(0, len(SeasonFromUntil)):
        html_string = SeasonFromUntil[_]
        soup = BeautifulSoup(str(html_string), 'html.parser')
        td_tag = soup.find("td", class_="zentriert")
        if td_tag:
            if _ % 3 == 0:  
                season_list.append(td_tag.text)
            if _ % 3 == 1:
                from_list.append(td_tag.text)
            if _ % 3 == 2:
                until_list.append(td_tag.text)
        else:
            print("NULL")

    for _ in range(0, len(Injury),2):
        html_string = Injury[_]
        soup = BeautifulSoup(str(html_string), 'html.parser')
        td_tag = soup.find("td", class_="hauptlink")
        if td_tag:
            injury_list.append(td_tag.text)
        else:
            print("NULL")

    for _ in range(0, len(DaysGamesMissed)):
        html_string = DaysGamesMissed[_]
        soup = BeautifulSoup(str(html_string), 'html.parser')
        td_tag = soup.find("td", class_="rechts")
        if td_tag:
            if _ % 2 == 0:  
                days_list.append(td_tag.text)
            if _ % 2 == 1:
                games_missed_list.append(td_tag.text)
        else:
            print("NULL")

    for _ in range(0, len(season_list)):
        player_id_list.append(player)

    return player_id_list, season_list, injury_list, from_list, until_list, days_list, games_missed_list

def GetPlayerProfile(player, pageSoup):
    player_name = pageSoup.find_all("h1", {"class":"data-header__headline-wrapper"})
    player_data = pageSoup.find_all("span", {"itemprop": True, "class":"data-header__content"})

    current_club_meta = pageSoup.find_all("span", {"class":"data-header__club" , "itemprop":"affiliation" })
    current_market_value_meta = pageSoup.find_all("div", {"class":"grid__cell grid__cell--center tm-player-transfer-history-grid__market-value"})
    current_market_value_meta = pageSoup.find_all("div.tm-player-transfer-history-grid__market-value")

    #SEEDING DATA
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

    player_id_list.append(player)

    club_soup = BeautifulSoup(str(current_club_meta[0]), 'html.parser')
    a_tag = club_soup.find('span', class_="data-header__club").find('a')
    club_name = a_tag.get('title')
    player_club_list.append(club_name)
    
    player_name_list.append(clean_player_name(player_name))

    current_market_value_list.append("NULL")

    for _ in range(0, len(player_data)):
            html_string = player_data[_]
            soup = BeautifulSoup(str(html_string), 'html.parser')
            td_tag = soup.find("span", class_="data-header__content")
            if td_tag:
                if _ % 4 == 0:  
                    date_of_birth_list.append(td_tag.text.strip())
                if _ % 4 == 1:
                    place_of_birth_list.append(td_tag.text.strip())
                if _ % 4 == 2:
                    citizenship_list.append(td_tag.text.strip())
                if _ % 4 == 3:
                    height_list.append(td_tag.text.strip())
            
            else:
                print("NULL")
    return player_id_list, player_club_list, player_name_list, date_of_birth_list, place_of_birth_list, citizenship_list, height_list, current_market_value_list