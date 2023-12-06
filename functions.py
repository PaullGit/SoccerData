
def GetPlayers(club_id, pageSoup):
    html_names = pageSoup.find_all("img", {"class": "bilderrahmen-fixed lazy lazy"})
    list_names = [element['alt'] for element in html_names] 

    html_ids = pageSoup.find_all("td", {"class": "rechts hauptlink"})
    list_ids = []
    
    for element in html_ids:
        html_id= str(element)
        parts = html_id.split("/")
        if len(parts) > 5:   
            player_id = parts[4].split(">")[0]
            cleaned_player_id = ''.join(char for char in player_id if char.isdigit())
        else: 
            player_id = "NULL"
        list_ids.append(cleaned_player_id)
    list_club_ids = [club_id for i in range(0, len(list_ids))]
    Validate (list_names, list_ids, club_id)
    return list_ids,list_names, list_club_ids


def Validate(a ,b, club_id):
    if len(a) != len(b):
        print("a: " + str( len(a)) )
        print("b: " + str( len(b)) )
        print("False on club_id: " + str(club_id))
        