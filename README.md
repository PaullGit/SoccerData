# SoccerData

 Transfermarkt Webscraping

 Zorg ervoor dat python geinstalleerd is op jouw device en dat de volgende extensies geinstalleerd zijn

``sudo pip3 install requests``

``sudo pip3 install bs4 ``

``sudo pip3 install pandas``

## All Players

Het "_all_players_" script is ontworpen om een lijst van alle spelers van geselecteerde voetbalclubs op Transfermarkt op te halen. Het verzamelt gegevens zoals SpelerID, SpelerNaam en ClubID en presenteert deze in een gestructureerde lijst.

* **SpelerID:** Een unieke identificatiecode voor de speler.
* **SpelerNaam:** De naam van de speler.
* **ClubID:** Een unieke identificatiecode voor de club waartoe de speler behoort.

Run `all_players.py` om een csv_bestand uit te rollen van alle spelers binnen de `geselecteerde voetbalclubs` 

## Injury History

Het "_player_injury_history_" script is ontworpen om de blessuregeschiedenis van specifieke voetbalspelers op Transfermarkt op te halen. Het verzamelt gegevens zoals BlessureID, SpelerID, BlessureType en de duur van de blessure.

* **BlessureID:** Een unieke identificatiecode voor de blessure.
* **SpelerID:** Een unieke identificatiecode voor de speler.
* **BlessureType:** Het type blessure dat de speler heeft opgelopen.
* **Duur:** De duur van de blessure.

Run `player_injury_history.py` om een csv_bestand uit te rollen van alle blessures van de spelers uit `all_players.csv`

## Profile

Het "_player_profile_" script is ontworpen om het profiel van specifieke voetbalspelers op Transfermarkt op te halen. Het verzamelt gegevens zoals SpelerID, SpelerNaam, Geboortedatum, Positie en Nationaliteit.

* **SpelerID:** Een unieke identificatiecode voor de speler.
* **SpelerNaam:** De naam van de speler.
* **Geboortedatum:** De geboortedatum van de speler.
* **Positie:** De positie van de speler op het veld.
* **Nationaliteit:** De nationaliteit van de speler.
* **ClubNaam:** Een naam voor de club waartoe de speler behoort.

Run `player_profile.py` om een csv_bestand uit te rollen van alle profielen van de spelers uit `all_players.csv`

## Functions
Hier staat alle gedetailleerde informatie over de functies die gebruikt worden in de bovenstaande scripts. 

## Utility Directory
Hier zijn een aantal functies die gebruikt worden in de andere scripts. 

* `stopwatch.py:` Een functie die de tijd meet die het kost om een script uit te voeren
* `leagues.py:` Beschikt over een lijst met alle ClubsID's per competitie.
* `toSQL.py:` Een functie die een csv bestand in een database stopt.

## Files
Hier staan een aantal resultaten in csv bestanden van de bovenstaande scripts.