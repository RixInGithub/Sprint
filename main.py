from gtts import gTTs as sprintspeech
import time
import tkinter

engine = sprintspeech.init()
rate = engine.setProperty("rate", 60)
print("Current rate: " + rate)
""" Sprint face showing 1 starts """
sprint1 = tkinter.Tk()
sprint1.title("Sprint")
sprintimage = PhotoImage(file="/sprint.png")
sprintshow1 = (sprint1, image=sprintimage, borderwidth=0)
sprint1.geometry("300x300")
""" Sprint face showing 1 ends """
engine.say("Hi. I am Sprint.")
engine.runAndWait()
engine.stop()
time.sleep(4)
""" Sprint face hiding 1 starts """
sprint1.destroy()
""" Sprint face hiding 1 ends """
