#!/bin/bash

blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'

# Package
py=$(dpkg -s sudo | head -n1)

#Python package
urllib=$(pip2 list | grep "urllib3")
color=$(pip2 list | grep "colorama")
bs=$(pip2 list | grep "bs4")
bl=$(pip2 list | grep "Blinder")

echo -e $green"[/] Checking Dependencies "
sleep 1
if [[ $py == *"Package: python2"* ]]; then
    echo -e $green"[:)] Python Package Already Installed "
else 
    echo -e $red"[!] Python2 Package not installed"
    echo -e $cyan"[/] installing python2 please wait.."
    sudo apt-get install python2 || apt-get install python2
fi



if [[ $urllib == *"urllib3"* ]]; then
    echo -e $green"[:)] Urllib3 Package Already Installed "
else
    echo -e $red"[!] Urllib3 Package not installed"
    echo -e $cyan"[/] installing urllib3 please wait.."
    sudo pip2 install urllib3 || pip2 install urllib3
fi


if [[ $color == *"colorama"* ]]; then
    echo -e $green"[:)] Colorama Package Already Installed "
else
    echo -e $red"[!] Colorama Package not installed"
    echo -e $cyan"[/] installing colorama please wait.."
    sudo pip2 install colorama || pip2 install colorama
fi

if [[ $bs == *"bs4"* ]]; then
    echo -e $green"[:)] Bs4 Package Already Installed "
else
    echo -e $red"[!] Bs4 Package not installed"
    echo -e $cyan"[/] installing bs4 please wait.."
    sudo pip2 install bs4 || pip2 install bs4
fi

if [[ $bl == *"Blinder"* ]]; then
    echo -e $green"[:)] Blinder Package Already Installed "
else
    echo -e $red"[!] Blinder Package not installed"
    echo -e $cyan"[/] installing bs4 please wait.."
    sudo pip2 install Blinder || pip2 install Blinder
fi

python2 sql.py
