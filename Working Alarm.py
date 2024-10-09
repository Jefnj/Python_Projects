# # Python Alarm Clock
import pygame
import time
import _datetime

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "be brave.mp3"
    is_running = True
    while is_running:
        current_time = _datetime.datetime.now().strftime("%H:%M:%S")                          # strftime is a format specifier
        print(current_time)
        if current_time == alarm_time:
            print("WAKE UP!😖")
            pygame.mixer.init()                                                        # mixer is library for loading and playing sounds
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False
        time.sleep(1)
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS)")
    set_alarm(alarm_time)




