import sqlite3
import pandas

df = pandas.read_csv('./files/player_profile.csv')

connection = sqlite3.connect('soccerdata.db')

df.to_sql('profile', connection, if_exists='replace') 