from bs4 import BeautifulSoup

def Validate(a ,b, club_id):
    if len(a) != len(b):
        print("a: " + str( len(a)) )
        print("b: " + str( len(b)) )
        print("False on club_id: " + str(club_id))

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
    Validate(list_names, list_ids, club_id)
    
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
    #PAGE SOUPING
    player_data = pageSoup.find_all("span", {"class":"info-table__content info-table__content--bold"})
    current_club_meta = pageSoup.find_all("span", {"class":"data-header__club" , "itemprop":"affiliation" })
    current_market_value_meta = pageSoup.find_all("div", {"class":"current-value svelte-18lvpom"}) 
    #SEEDING DATA
    player_id_list = []
    date_of_birth_list = []
    place_of_birth_list = []
    citizenship_list = []
    height_list = []

    name_in_country_list = []
    position_list = []
    foot_list = []

    current_club_list = []
    current_market_value_list = []
    
    player_id_list.append(player)
    current_club_list.append(current_club_meta[0].text.strip())
    current_market_value_list.append("NULL")
    if hasCountryName(player_data[0]):
        for _ in range(0, 7):
                html_string = player_data[_]
                soup = BeautifulSoup(str(html_string), 'html.parser')
                td_tag = soup.find("span", class_="info-table__content info-table__content--bold")   

                if td_tag:
                    if _ % 8 == 0:  
                        name_in_country_list.append(td_tag.text.strip())
                    if _ % 8 == 1:
                        date_of_birth_list.append(td_tag.text.strip())
                    if _ % 8 == 2:
                        place_of_birth_list.append(td_tag.text.strip())
                    if _ % 8 == 3:
                        height_list.append(td_tag.text.strip()) 
                    if _ % 8 == 4:
                        citizenship_list.append(td_tag.text.strip())
                    if _ % 8 == 5:
                        position_list.append(td_tag.text.strip())
                    if _ % 8 == 6:  
                        foot_list.append(td_tag.text.strip())
                else:
                    print("NULL")
    else:
        for _ in range(0, 6):
                html_string = player_data[_]
                soup = BeautifulSoup(str(html_string), 'html.parser')
                td_tag = soup.find("span", class_="info-table__content info-table__content--bold")   

                if td_tag:
                    if _ % 7 == 0:  
                        date_of_birth_list.append(td_tag.text.strip())
                    if _ % 7 == 1:
                        place_of_birth_list.append(td_tag.text.strip())
                    if _ % 7 == 2:
                        height_list.append(td_tag.text.strip()) 
                    if _ % 7 == 3:
                        citizenship_list.append(td_tag.text.strip())
                    if _ % 7 == 4:
                        position_list.append(td_tag.text.strip())
                    if _ % 7 == 5:  
                        foot_list.append(td_tag.text.strip())
                else:
                    print("NULL")
        return player_id_list, name_in_country_list, date_of_birth_list, place_of_birth_list, height_list, citizenship_list, foot_list, current_club_list, current_market_value_list

def hasCountryName(first):
    soup = BeautifulSoup(str(first), 'html.parser')
    td_tag = soup.find("span", class_="info-table__content info-table__content--bold")

    if td_tag.text.strip() == "Name in home country:":
        return False
    else:
    