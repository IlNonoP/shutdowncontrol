from flask import Flask, request
import os
import sys



path="/opt/shutdowncontrol/"


args = sys.argv[1:]
G
reiceved_port = args[0]
reiceved_password = args[1]
version = args[2]


if reiceved_port == "-":
    port = 5000
else:
    port = int(reiceved_port)

if reiceved_password == "-":
    password = "-"
else:
    password = reiceved_password

print("\nShutdownControl V. "+version+"\n")
print("Starting server on port="+str(port))
if password != "-":
    print("Request password="+password)

print("\n\nApp debug:")



os.system("rm "+path+"lock_file/*")

try:
    os.system(f"mkdir {path}lock_file")
except:
    print("Direcory already exist")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_form():
    # legge i campi form "id" e "data" e "password"
    data = request.form.get('data')
    action = request.form.get('action')
    login = request.form.get('password')
    
   
    if password == "-" or password == login:
        if action == "lock":
            if os.path.isfile(path+"/lock_file/"+data) == True:
                return "Error, a locked file whit this ID already exist"+"\n"
                
            elif os.path.isfile(path+"/lock_file/"+data) == False:
                os.system("touch "+path+"lock_file/"+data)
                return "Shutdown locked whit the ID: "+data+"\n"





        elif action =="unlock":
            if os.path.isfile(path+"/lock_file/"+data) == False:
                return "Error, there is no lock file whit is ID"+"\n"

            elif os.path.isfile(path+"/lock_file/"+data) == True:
                os.remove(path+"lock_file/"+data)
                return "Shutdown unlocked for ID: "+data+"\n"


        else:
            return 'Error, invalid action, you must use "lock" or "unlock"\n'
    else:
        return("Error, password is wrong")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)
