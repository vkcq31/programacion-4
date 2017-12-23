from tweepy import Stream, OAuthHandler, API, Cursor
from tweepy.streaming import StreamListener
import sqlite3

cke = "2HfPnv52ONh60VEDNu88i2tXq"
cse = "I1HkpJtJPdqDNawUxGCPoHsC1JjyQ6Mpeuf4kg3vxRJ9bwdk7Q"
ato = "915031736454713344-R9Xlvkuou0hNWHcrcXy8LaOLt2wgefl"
ase = "qmGOsRB1KwY1ZZJQBZ2qH7btKyGA1TDKL5xXmupRzy02m"

auth = OAuthHandler(cke, cse)
auth.set_access_token(ato, ase)


class TLListener(StreamListener):
    def on_data(self, raw_data):
        print(raw_data)
        return True

    def on_error(self, status_code):
        print(status_code)

twStream = Stream(auth, TLListener())
twStream.filter(track=["#PrayForVegas"])

db = sqlite3.connect('twitter.db')

cursor = db.cursor()
cursor.execute('''CREATE TABLE tweet(id INTEGER PRIMARY KEY,
                  tweet TEXT, usuario TEXT)''')

usuario = input("")
tweet = input("")
cursor.execute('''INSERT INTO tweet (id, tweet, usuario) VALUES 
                  (?,cifrar(?))''', (usuario, tweet, id()))
db.commit()




