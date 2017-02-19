import os,sys,time
import platform
import subprocess
    

def close():
        os.system("TASKILL /F /IM Mycam.exe")

def run(app):
    time.sleep(2)
    result = os.startfile(app)
    time.sleep(10)
    close()

def opSys(place):
    if platform.system() == 'Windows':
        
        run(place)
    elif platform.system() == 'Linux':
        run(place)

    


def main():
    point = input("place the path to the camera you want to start with your system: ")
    opSys(point)
main()
            


#C:\Users\Hamza Bashir\Desktop\MyCam\MyCam.exe
            
    

            
        

    #subprocess.call(["cmd.exe", tasklist])
    #Taskkill /PID 3584 /F


    #pid 3584
'''decide on the os that is used on the system, if windows, locate the webcam,
if linux, locate the webcam'''
'''if windows, add the shortcut of the file to the startup folder'''
'''for linux, make it start on startup'''
'''to close down, we can do that later'''

    
