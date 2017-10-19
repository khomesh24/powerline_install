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



if __name__ == '__main__':
    print("main")
    set_hostname()