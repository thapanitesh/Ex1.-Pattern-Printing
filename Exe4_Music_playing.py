from pygame import*
def play_music(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
while True:
    select = input("Press w for water, e for eyes and p for exercise\n")
    if select == "w": 
        file = "/Users/niteshthapa/Desktop/Python Tutorial/Water.ogg" 
        play_music(file)
        while True:
            command = input("Enter p as pause , r as resume and s as stop\n")
            if command == "p":
                mixer.music.pause()
            elif command == "r":
                mixer.music.unpause()
            elif command == "s":
                mixer.music.stop()
                break
        break
    elif select == "e":
        file = "/Users/niteshthapa/Desktop/Python Tutorial/Eyes .ogg"
        play_music(file)
        while True:
            command = input("Enter p as pause , r as resume and s as stop\n")
            if command == "p":
                mixer.music.pause()
            elif command == "r":
                mixer.music.unpause()
            elif command == "s":
                mixer.music.stop()
                break
        break                  
    elif select == "p":
        file = "/Users/niteshthapa/Desktop/Python Tutorial/Workout Music Mix ft. ONLAP.ogg"
        play_music(file)
        while True:
            command = input("Enter p as pause , r as resume and s as stop\n")
            if command == "p":
                mixer.music.pause()
            elif command == "r":
                mixer.music.unpause()
            elif command == "s":
                mixer.music.stop()
                break 
        break         

