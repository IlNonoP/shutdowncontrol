import os
path="/opt/shutdowncontrol/"

while True:
    if os.listdir(path+"lock_file/") == []:
        print("No lock file found")
        break
    else:
        print("Locked file found")
    os.system("sleep 1")
print("shoutdowncontroller terminate\n")