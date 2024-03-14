import os
from tkinter import *
from gtts import gTTS
from playsound import playsound
import threading
from tkinter.ttk import Progressbar

def Text_to_speech():
    Message = entry_field.get()
    if Message:
        speech = gTTS(text=Message)
        if os.path.exists('DataFlair.mp3'):
            os.remove('DataFlair.mp3')
        speech.save('DataFlair.mp3')

        # Start the progress bar
        progress_bar.start(10)
        microphone_label.config(text='🎤 Speaking...')
        # Create a separate thread for playing the sound
        play_thread = threading.Thread(target=play_sound)
        play_thread.start()

def play_sound():
    playsound('DataFlair.mp3')
    microphone_label.config(text='🎤 Speak')
    # Stop the progress bar
    progress_bar.stop()

def Exit():
    if os.path.exists('DataFlair.mp3'):
        os.remove('DataFlair.mp3')
    root.destroy()


def Reset():
    Msg.set("")

root = Tk()
root.geometry('700x400')
root.resizable(0, 0)
root.config(bg='ghost white')
root.title('DataFlair - TEXT_TO_SPEECH')

Label(root, text='TEXT TO SPEECH', font='arial 20 bold', bg='white smoke').pack()
Label(root, text='text-to-speech', font='arial 15 bold', bg='white smoke').pack(side=BOTTOM)

Label(root, text='Enter Text :', font='arial 15 bold', bg='white smoke').place(x=30, y=60)

Msg = StringVar()
entry_field = Entry(root, textvariable=Msg, width='90')
entry_field.place(x=40, y=100)

Button(root, text="PLAY", font='arial 15 bold', command=Text_to_speech, width=4).place(x=150, y=140)
Button(root, text='EXIT', font='arial 15 bold', command=Exit, bg='OrangeRed1').place(x=250 ,y=140)
Button(root, text='RESET', font='arial 15 bold', command=Reset).place(x=350, y=140)

microphone_label = Label(root, text='🎤 Speak:', font=('arial', 14), bg='white')
microphone_label.place(x=250, y=195)
progress_bar = Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')
progress_bar.place(x=60, y=230)

root.mainloop()
