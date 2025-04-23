import sys
import subprocess
import os

path="/opt/shutdowncontrol/"

def main():
    args = sys.argv[1:]
    if args == []:
        print("Error, no args add, use shutdowncontrol help for a guide")
        return

        
    if args[0] == "start":
        try:            
            port = args[1]
            print("I'm using "+port +" port")
            os.system("python3 server.py "+port)

        except:
            print("No port specified, 5000 will used")
            os.system("python3 server.py")
    elif args[0] == "watch":
        os.system("python3 watch.py")
    elif args[0] == "help":
        print("Usage:")
        print("shoutdowncontrol [arg] ")
        print("                    |-  start [port]                   This command start the server at the specified port")
        print("                    |            |_ port  ex: 5000     This number is the number of the port you will send the requests")
        print("                    |-  watch                          This command is used for verify if there are any file lock. The program will continue only if tyhere isn't any lock, if tehere are any lock the program will not continue")
        print("                    |_  help                           Show this guide")
    else:
        print('Error, invalid command, use "shoutdowncontrol help" to see the guide')

    

if __name__ == "__main__":
    os.chdir(path)
    main()
