#!/usr/bin/python3

'''This is to install basic software after fresh installation of fedora'''
import os

def update():
    print("system updating")
    #os.system("dnf update")
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

if __name__ == '__main__':
    print("main")
    #update()
    #set_hostname()
    #add_tweak()
    add_rpmfusion()
