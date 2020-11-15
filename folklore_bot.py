# Author: Liplan Lekipising
# Created: 15th November, 2020

from folklore_lyrics import master_list

import datetime
import random
import schedule
import time


def lyric():
    print()
    songs = []
    for song in master_list:
        songs.append(song)
    
    r_song = random.choice(songs)
    for k, v in master_list.items():
        if k == r_song:
            print(random.choice(v))
            print()
            print('Lyrics from ' + k)
    

schedule.every(60).minutes.do(lyric)

while True:
    schedule.run_pending()
    time.sleep(1)
