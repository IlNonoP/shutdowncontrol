import os
path="/opt/shutdowncontrol/"

while True:
    try:
        file = os.listdir(path+"lock_file/")
        if os.listdir(path+"lock_file/") == []:
            print("No lock file found")
            break
        else:
            print("Locked file found")
    except:
        pass
    
    os.system("sleep 1")
print("shoutdowncontroller terminate\n")
