from flask import Flask, request
import os
import sys



path="/opt/shutdowncontrol/"


try:
    args = sys.argv[1:]
    port = args[0]
except:
    port = 5000

os.system("remove "+path+"lock_file/*")

try:
    os.makedirs(path+"lock_file")
except:
    print("Direcory already exist")

app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive_form():
    # legge i campi form "id" e "data"
    data = request.form.get('data')
    action = request.form.get('action')
    
   

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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port, debug=True)