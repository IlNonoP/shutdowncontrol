#!/bin/bash
git clone https://github.com/IlNonoP/shutdowncontrol.git
cd shutdowncontrol
echo First leaning
rm LICENSE 
rm README.md  
rm -rf .git
rm *.sh
echo Installation...
mv shutdowncontrol /usr/local/bin/shutdowncontrol
sudo chmod +x /usr/local/bin/shutdowncontrol
mkdir /opt/shutdowncontrol
mv * /opt/shutdowncontrol
cd ..
echo Final cleaning...
rm -rf shutdowncontrol
echo Finished!!!
rm install.sh
