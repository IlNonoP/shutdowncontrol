# ShutdownControl
This is a small CLI program that allows a script to be prevented from continuing if there are blockages, example prevents the computer from shutting down if some programs are running.

## Features
- Blocking by curl request
- Unlocking by curl request
- Supports multiple blocks simultaneously
- Support for password verification to avoid unwanted locks or unlocks

## Installation
For a quick installation just use the script given, use this command to download and run it, or download it from the repository

```bash
wget https://raw.githubusercontent.com/IlNonoP/shutdowncontrol/main/install.sh && sudo bash install.sh
```
  

## Uninstallation
For a quick uninstallation just use the script given, use this command to download and run it, or download it from the repository
```bash
wget https://raw.githubusercontent.com/IlNonoP/shutdowncontrol/main/uninstall.sh && sudo bash uninstall.sh
```

## Usage
### Start server
Use is simple, once the program is installed you can start the server to receive lock and unlock requests. Use
```bash
shutdowncontrol start
```
to start it up. To choose a port other than the default (5000) you can specify it after the start command as in this example where 3004 is used

```bash
shutdowncontrol start 3004
```
If you want to set a password to send lock or unlock requests add ```p=[password]```, in this example pippo will be used as the password

```bash
shutdowncontrol start p=pippo
```


### Send request
Curl can be used to send lock and unlock requests.

To send blocking requests, it is necessary to use
```bash
curl -d "action=[lock/unlock]" -d "data=[id]" -d "password=[password]" http(s)://[address]:[port]/     
```
The varible data in this command are:
- [lock/unlock] = Based on whether you want to send a lock (lock) or unlock (unlock) request
- [id] = Chosen by the user, it is used to identify the blocking request and remove the specific one
- [address] = Server address *
- [port] = Server port *
- [password] = Optional, but increases security. Note that it is necessary to write the password attached to the equal and the p. In case there is no password you can directly remove this part ```-d ”password=[password]“```

*In case you do not know where to find this data, it is shown when the server starts up

### Check whether it is possible to turn off
Let's get to the juicy part of the talk. Let's say we have a script launched at system startup that shuts down our computer after an hour. We will have a script like this:
```bash
#!/bin/bash

sleep 3600    #Wait one hour
poweroff      #Turn off the computer
```
 Now let's say that sometimes we want something to end before we turn everything off, but this thing takes more than an hour. We can integrate shutdowncontrol into our script with a simple command
```bash
#!/bin/bash

sleep 3600    #Wait one hour
shutdowncontrol watch    #Verify if he can turn off the computer
poweroff      #Turn off the computer
```
This command will check whether any locks have been set, that is, it will check whether any lock requests have been received. If there are not it will continue program execution, i.e. it will shut down the computer. Otherwise, if there are locks, it will wait for them to be removed before continuing the program.

## Conclusion
I hope the guide is clear, if you have any doubts or questions or find BUGs please feel free to mark them!!
