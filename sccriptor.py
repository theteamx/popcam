import os,sys,time
import subprocess
import signal

class Application:
    def __init__(self):
        pass
        
    def run():
        app = os.startfile('C:\Users\Hamza Bashir\Desktop\MyCam\MyCam.exe')
    run()

    def close():
        proc = time.sleep(5)
        proc = subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
        stdout = proc.communicate('Taskkill /IM Mycam.exe /F')
    close()
        
        

    #subprocess.call(["cmd.exe", tasklist])
    #Taskkill /PID 3584 /F


    #pid 3584

    
