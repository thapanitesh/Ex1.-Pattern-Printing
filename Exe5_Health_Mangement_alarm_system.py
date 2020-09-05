from pygame import mixer
import datetime
from time import localtime
import time
def date_time():
    return datetime.datetime.now()
def play_music(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
start_time = localtime().tm_hour
init_water = time.time()
init_eyes = time.time()
init_execrise = time.time()
watersec = 1800
eyessec = 2700
exesec = 3600
driking_water_lit = 0
while True:
    if start_time >= 9 and start_time <= 17:
        if driking_water_lit < 3.5:
            if time.time()-init_water>watersec:
                file = "/Users/niteshthapa/Desktop/Python Tutorial/Water.ogg"
                play_music(file)
                while True:
                    music_stop = input("Enter drank to stop music:\n")
                    if music_stop == "drank":
                        mixer.music.stop()
                        with open("water_drank.txt", "a") as f:
                            f.write(str([str(date_time())])+":"+"drank water 0.5 liter"+"\n")
                            driking_water_lit = driking_water_lit + 0.5
                            init_water = time.time()
                            break
        if time.time()-init_eyes>eyessec:
            file = "/Users/niteshthapa/Desktop/Python Tutorial/Eyes .ogg"
            play_music(file)
            while True:
                music_stop = input("Enter eydone to stop music:\n")
                if music_stop == "eydone":
                    mixer.music.stop()
                    with open("eyedone.txt", "a") as f:
                        f.write(str([str(date_time())])+":"+"eye exercise is done"+"\n")
                        init_eyes = time.time()
                        break
        if time.time()-init_execrise>exesec:
            file = "/Users/niteshthapa/Desktop/Python Tutorial/Workout Music Mix ft. ONLAP.ogg"
            play_music(file)
            while True:
                music_stop = input("Enter phydone to stop music:\n")
                if music_stop == "phydone":
                    mixer.music.stop()
                    with open("phydone.txt", "a") as f:
                        f.write(str([str(date_time())])+":"+"physcial exercise is done"+"\n")
                        init_execrise = time.time()
                        break