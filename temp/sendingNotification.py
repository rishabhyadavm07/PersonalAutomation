# from win10toast import ToastNotifier
# from cProfile import label
# from win10toast import ToastNotifier
from winotify import Notification, audio
# toaster = ToastNotifier()
# toaster.show_toast("Title", "Message", duration=5)
print("rishabh")

toast = Notification(app_id="Personal Automation",
                    title="Just ran a automation",
                    msg="Tell me what is occupying your attentional space ? ",
                    duration="short",
                    icon=r"C:\Users\Rishabh\Desktop\AutomationLogo.png")


# toast.add_actions(label="Click me!", launch="https://impyadav.com")
# toast.add_actions
t = 
# toast.set_audio(audio.SMS, loop=False)
# toast.set_audio(audio.Mail, loop=False)
# toast.add_actions(label="rishabh")
# toast.set_audio(audio.LoopingAlarm, loop=True)
toast.set_audio(audio.LoopingCall, loop=True)
# toast.set_audio(audio.Default, loop=False)

toast.show()