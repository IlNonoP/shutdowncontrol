import sys
import subprocess
import os

version="1.1"

path="/opt/shutdowncontrol/"

def main():
    args = sys.argv[1:]
    if args == []:
        print("Error, no args add, use shutdowncontrol help for a guide")
        return

        
    if args[0] == "start":
        try:
            arg1=args[1]            
            try:               
                arg2=args[2]                
            except:                
                arg2 = "-"
           

            if "p=" in arg1:                
                commodo = arg2
                password = arg1
                port = commodo
            else:
                password = arg2
                port = arg1            
            if port != "-":                
                comando = "python3 server.py "+port+" "
            else:                
                comando = "python3 server.py - "            
            if "p=" in password:
                
                password = password.replace("p=", "")
                
                if password == "-":
                    print("\nERROR\nYou cant use this password, change it please")
                    exit()
                comando = comando + password + " "
            else:
                
                comando = comando + "- "
           
            os.system(comando + version)

        except:
            print("No port specified or password specified, 5000 will used")
            os.system("python3 server.py - - "+version)


    elif args[0] == "watch":
        os.system("python3 watch.py")
    elif args[0] == "help":
        print("ShutdownContol V. "+version)
        print("")
        print("Usage:")
        print("shoutdowncontrol [arg] ")
        print("                    |-  start [args]                   This command start the server at the specified port")
        print("                    |            |- [port]  ex: 5000     (OPTIONAL!) (Default=5000) This number is the number of the port you will send the requests")
        print("                    |            |_ p=[password] ex: 123 (Optional!) (Default=Disable) This topic allows you to add a password to avoid unapproved requests")
        print("                    |-  watch                          This command is used for verify if there are any file lock. The program will continue only if tyhere isn't any lock, if tehere are any lock the program will not continue")
        print("                    |_  help                           Show this guide")  
        print("")
        print("Command example:")
        print("shoutdowncontrol 5050                  Start shutdowncontrol server on 5050 port")
        print("shuutdowncontrol 5050 p=pippo           Start the server on 5050 port and use pippo as password")
        print("")
        print("See https://github.com/IlNonoP/shutdowncontrol for a complete guide, and for report bug")
    else:
        print('Error, invalid command, use "shoutdowncontrol help" to see the guide')

    

if __name__ == "__main__":
    os.chdir(path)
    main()
