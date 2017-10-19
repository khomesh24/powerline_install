#!/usr/bin/python3

'''This is to install basic software after fresh installation of fedora'''
import os

def update():
    print("system updating")
    os.system("dnf update")
    print("system updated")

def set_hostname():
    print("current host name is : ")
    os.system("hostname")
    print()
    if (input("want to change hostname [y/n]: ") == 'y' ):
        os.system("systemctl set-hostname \""+str(input("enter hostname: "))+"\"")

def add_tweak():
    os.system("dnf install gnome-tweak-tool")

def add_rpmfusion():
    os.system("rpm -ivh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-26.noarch.rpm")

def install_chrome():
    chrome_repo = open("/etc/dnf.repos.d/google-chrome.repo","w")
    content="[google-chrome] \nname=google-chrome - \$basearch \nbaseurl=http://dl.google.com/linux/chrome/rpm/stable/\$basearch \nenabled=1 \ngpgcheck=1 \ngpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub"
    chrome_repo.write(content)
    print("Enable Google DNF repo")
    os.system("dnf install google-chrome-stable")

def install_java_plugins():
    os.system("# dnf install java-openjdk icedtea-web")

if __name__ == '__main__':
    print("main")
    #update()
    #set_hostname()
    #add_tweak()
    #add_rpmfusion()
    #install_chrome()
    install_java_plugins()