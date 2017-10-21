#!/usr/bin/python3

'''This is to install basic software after fresh installation of fedora'''


import os

class get_started:
    def __init__(self):
        self.update()
        self.set_hostname()
        self.add_tweak()
        self.add_rpmfusion()
        self.install_chrome()
        self.install_java_plugins()
        self.install_spotify()
        self.add_powerline()
        self.add_vim_powerline()

    def update(self):
        print("system updating")
        os.system("dnf update -yq")
        print("system updated")

    def set_hostname(self):
        print("current host name is : ")
        os.system("hostname")
        print()
        if (input("want to change hostname [y/n]: ") == 'y' ):
            os.system("systemctl set-hostname \""+str(input("enter hostname: "))+"\"")

    def add_tweak(self):
        os.system("dnf install gnome-tweak-tool -y")

    def add_rpmfusion(self):
        os.system("rpm -ivh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-26.noarch.rpm")

    def install_chrome(self):
        chrome_repo = open("/etc/dnf.repos.d/google-chrome.repo","w")
        content="[google-chrome] \nname=google-chrome - \$basearch \nbaseurl=http://dl.google.com/linux/chrome/rpm/stable/\$basearch \nenabled=1 \ngpgcheck=1 \ngpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub"
        chrome_repo.write(content)
        print("Enable Google DNF repo")
        os.system("dnf install google-chrome-stable -y")

    def install_java_plugins(self):
        os.system("# dnf install java-openjdk icedtea-web -y")

    def install_spotify(self):
        os.system("dnf config-manager --add-repo=http://negativo17.org/repos/fedora-spotify.repo")
        os.system("dnf install spotify-client -y")

    def add_powerline(self):
        os.system("dnf install powerline powerline-fonts")
        content="\nif [ -f `which powerline-daemon` ]; then \n  powerline-daemon -q \n  POWERLINE_BASH_CONTINUATION=1 \n  POWERLINE_BASH_SELECT=1 \n   . /usr/share/powerline/bash/powerline.sh \n fi"
        file=open("/root/.bashrc","a")
        file.write(content)

    def add_vim_powerline(self):
        os.system("dnf install vim-powerline")
        content = ( "\npython3 from powerline.vim import setup as powerline_setup"
                    "\npython3 powerline_setup()"
                    "\npython3 del powerline_setup"
                    '\nset laststatus=2 " Always display the statusline in all windows'
                    '\nset showtabline=2 " Always display the tabline, even if there is only one tab'
                    '\nset noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline)'
                    '\nset t_Co=256'
                    '\nset number'
                    '\nset mouse=a'
        )
        with open("/root/.vimrc","a") as fobj:
            fobj.write(content)


if __name__ == '__main__':
    get_started
