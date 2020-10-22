# Yacht-DigitalOcean

## Info
This is just the scripts and instructions I'm using to setup my digitalocean image.

## Steps

1. `apt update -y && apt upgrade -y && shutdown -r now`
2. Install docker following this guide: https://docs.docker.com/engine/install/ubuntu/
3. `git clone https://github.com/SelfhostedPro/Yacht-DigitalOcean.git /opt/SelfhostedPro/`
4. `ufw allow 22 && ufw --force enable`
5. `cd /opt/SelfhostedPro/`
6. ```
    sudo apt-get update
    sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg-agent \
        software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io
    ```
7. `echo "/opt/SelfhostedPro/install_yacht.sh" >> /root/.bashrc`
8. `/opt/SelfhostedPro/img_check.sh`
9. `/opt/SelfhostedPro/cleanup.sh`
10. `/opt/SelfhostedPro/img_check.sh`
