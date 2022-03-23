
Follow the steps on the official docker documentation to install docker on ubuntu 
https://docs.docker.com/engine/install/ubuntu/.

```shell
#!/bin/bash
# Warning this instruction are the ones from docker.com in Mars 2022
# please get the latest instructions direct at
#https://docs.docker.com/engine/install/ubuntu/

# Check kernel version
echo "I am using"
uname -a

# Update package list
sudo apt-get update

# Install basic packages
sudo apt-get install ca-certificates curl gnupg lsb-release

# Add docker repo gpg key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add the docker repo to your apt-get sources
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update the package list, now it should include docker-ce
sudo apt-get update

# Install docker-ce with CLI and containerd.io
sudo apt-get install docker-ce docker-ce-cli containerd.io

```
