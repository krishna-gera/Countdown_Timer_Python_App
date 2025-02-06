import time
import tkinter as tk
from tkinter import simpledialog
from playsound import playsound

def play_sound():
    playsound('tone.mp3')

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        timer_label.config(text=timer)
        root.update()
        time.sleep(1)
        seconds -= 1

    timer_label.config(text="Time's up!")
    play_sound()

def start_timer():
    seconds = simpledialog.askinteger("Input", "Enter the time in seconds:")
    if seconds is not None:
        countdown_timer(seconds)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Countdown Timer")

    timer_label = tk.Label(root, font=('Helvetica', 48), text="00:00")
    timer_label.pack(pady=20)

    start_button = tk.Button(root, text="Start Timer", command=start_timer)
    start_button.pack(pady=20)

    root.mainloop()
