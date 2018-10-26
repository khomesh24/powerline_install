#!/usr/bin/python3

'''This is to install basic software after fresh installation of fedora'''
'''Maintainer: Khomesh Thakre'''

import os

class get_started:
    def __init__(self):
        print("Hold tight, it may take some time!")
        self.update()
        self.set_hostname()
        self.add_tweak()
        self.add_rpmfusion()
        self.install_chrome()
        self.install_java_plugins()
	    self.install_nodejs()
        self.install_spotify()
        self.add_powerline()
        self.add_vim()
        self.add_vim_powerline()
        self.install_docker()
        self.install_pycharm()
        self.install_openssh()
        self.install_atom()
        self.install_cmake()
        self.install_docker_ce()
        self.create_ssh_key()
        self.supplemental_fedora28_wallpapers()
        self.fastboot()
        

    def update(self):
        print("System updating......")
        os.system("dnf update -yq")
        print("System updated successfully")

    def set_hostname(self):
        print("Setting up Hostname \nThe current host name is : ")
        os.system("hostname")
        if (input("Do you want to change the current hostname? [y/n]: ") == 'y' ):
            os.system("systemctl set-hostname \""+str(input("Enter hostname: "))+"\"")
            print("Your hostname is now changed to: ")
            os.system("hostname")

    def add_tweak(self):
        print("Installing Gnome-tweak tool......")
        os.system("dnf install gnome-tweak-tool -y")
        print("Gnome-tweak tool installation completed")

    def add_rpmfusion(self):
        print("Adding rpmFusion ......")
        os.system("rpm -ivh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-26.noarch.rpm")
        print("rpmFusion is added")

    def install_chrome(self):
        print("Installing Google-Chrome......")
        chrome_repo = open("/etc/dnf.repos.d/google-chrome.repo","w")
        content="[google-chrome] \nname=google-chrome - \$basearch \nbaseurl=http://dl.google.com/linux/chrome/rpm/stable/\$basearch \nenabled=1 \ngpgcheck=1 \ngpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub"
        chrome_repo.write(content)
        print("Enabling Google DNF repo......")
        os.system("dnf install google-chrome-stable -y")
        print("Google-Chrome installation completed")

    def install_java_plugins(self):
        print("Installing java packages......")
        os.system("# dnf install java-openjdk icedtea-web -y")
        print("Java installation completed")

    def install_spotify(self):
        print("Installing Spotify......")
        os.system("dnf config-manager --add-repo=http://negativo17.org/repos/fedora-spotify.repo")
        os.system("dnf install spotify-client -y")
        print("Spotify installation completed")

    def add_powerline(self):
        print("Adding powerLine to gnome-terminal......")
        os.system("dnf install powerline powerline-fonts")
        content="\nif [ -f `which powerline-daemon` ]; then \n  powerline-daemon -q \n  POWERLINE_BASH_CONTINUATION=1 \n  POWERLINE_BASH_SELECT=1 \n   . /usr/share/powerline/bash/powerline.sh \n fi"
        file=open("/root/.bashrc","a")
        file.write(content)
        print("Powerline is added")

    def add_vim(self):
        print("Adding vim ......")
        os.system("dnf install -y vim-enhanced")

    def add_vim_powerline(self):
        print("Adding powerLine to Vim......")
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
        print("Powerline is added to Vim")

    def install_docker(self):
        print("Installing Docker......")
        os.system("rpm -ivh https://download.docker.com/linux/fedora/26/x86_64/stable/Packages/docker-ce-17.09.0.ce-1.fc26.x86_64.rpm")
        print("Docker installation completed")

    def install_pycharm(self):
        print("Installing PyCharm......")
        os.system("""echo [phracek-PyCharm]
name=Copr repo for PyCharm owned by phracek
baseurl=https://copr-be.cloud.fedoraproject.org/results/phracek/PyCharm/fedora-$releasever-$basearch/
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://copr-be.cloud.fedoraproject.org/results/phracek/PyCharm/pubkey.gpg
enabled=1
enabled_metadata=1 > /etc/yum.repos.d/pycharm.repo""")
        os.system("dnf copr enable phracek/PyCharm")
        os.sytem("dnf -y install pycharm-community")
        print("PyCharm installation completed")

    def install_openssh(self):
        print("Installing OpenSSH......")
        os.system("dnf install -y openssh-server")
        os.system("systemctl start sshd.service")
        os.system("systemctl enable sshd.service")
        print("OpenSSH installation completed")
            
    def install_atom(self):
        print("Installing Atom")
        os.system("rpm --import https://packagecloud.io/AtomEditor/atom/gpgkey")
        os.system("rpm --import https://packagecloud.io/AtomEditor/atom/gpgkey")
        os.system("dnf -y install atom")
        print("Atom installation completed")
    
    def install_cmake(self):
        print("Installing cmake ...")
        os.system("yum -y install cmake")
        print("Cmake installation completed")
        
    def install_vsCode(self):
        print("Installing VS Code")
        os.system("rpm --import https://packages.microsoft.com/keys/microsoft.asc")
        os.system("""sh -c 'echo -e "[code]\nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc" > /etc/yum.repos.d/vscode.repo'""")
        os.system("dnf check-update")
        os.system("dnf install code")
        print("VS Code installation completed")
       
    def install_docker_ce(self):
        print("Installing Docker Community Edition...")
        os.system("dnf -y install dnf-plugins-core")
        os.system("dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo")
        os.system("dnf install docker-ce")
        os.system("systemctl start docker")
        print("Docker-CE installation completed.")

    def create_ssh_key(self):
    	print("Creating SSH key...")
    	os.system('HOSTNAME=`hostname` ssh-keygen -t rsa -C "$HOSTNAME" -f "$HOME/.ssh/id_rsa" -P "" && cat ~/.ssh/id_rsa.pub')
    	print("Creating SSH Key is completed.")

    def supplemental_fedora28_wallpapers(self):
    	print("Installing Fedora 28 Supplemental Wallpapers")
    	os.system("dnf install f28-backgrounds-extras-gnome")
    	print("Fedora 28 Supplemental Wallpapers installation completed.")

    def fastboot(self):
		print("Installing fastboot")
    	os.system("dnf install fastboot")
    	print("Fastboot installation completed.")

    def fastboot(self):
		print("Installing fastboot")
    	os.system("dnf install fastboot")
    	print("Fastboot installation completed.") 

     def supplemental_fedora28_wallpapers(self):
    	print("Installing Fedora 28 Supplemental Wallpapers")
    	os.system("dnf install f28-backgrounds-extras-gnome")
    	print("Fedora 28 Supplemental Wallpapers installation completed.")   	
        

if __name__ == '__main__':
    get_started()
