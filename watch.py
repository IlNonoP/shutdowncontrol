import os
path="/opt/shutdowncontrol/"

try:
    os.makedirs(path+"lock_file")
except:
    print("Direcory already exist")
    
while True:
    if os.listdir(path+"lock_file/") == []:
        print("No lock file found")
        break
    else:
        print("Locked file found")
    os.system("sleep 1")
print("shoutdowncontroller terminate\n")
