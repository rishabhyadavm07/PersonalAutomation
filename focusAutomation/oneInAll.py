
import time
from winotify import Notification, audio
from tkinter import *
#IMPORTANT FUNCTIONS
def submit():
    global data
    data = entry.get()

# starting with time phase
current_time = time.ctime()

def writeToFile(vartoWrite):
    file = open(r"C:\Users\Rishabh\Desktop\automationProjects\personalAutomation\focusAutomation\output\demo.txt", "a")#CHANGE ACCORDING TO YOU
    file.write("\n"+vartoWrite)
    file.close()



done = "\nDone "#will be used for testing only


#sending notifications
#PLEASE CHANGE THE BELOW ACCORDING TO YOU
toast = Notification(app_id="Personal Automation",
                    title="Foodie:",
                    msg="Tell me what is occupying your attentional space ? ",
                    duration="short",
                    icon=r"C:\Users\Rishabh\Desktop\AutomationLogo.png")#CHANGE ACCORDING TO YOU


toast.set_audio(audio.LoopingCall, loop=True)
toast.show()

#taking input with GUI dialog box
window = Tk()
#creating a buttton
submit = Button(window,text="Save",command=submit)
submit.pack(side = RIGHT)

entry = Entry()
entry.config(font=('Mono', 30),bg='Black', fg='Green')

entry.pack()
window.mainloop()

#writing the data collected to the end file
writeToFile(current_time)
writeToFile(data)
# writeToFile(done)