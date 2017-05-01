### Check conditions

## check kernel
uname -a

## check Divice Mapper
ls -l /sys/class/misc/device-mapper 

# check in proc
sudo grep device-mapper /proc/devices

# load divice mapper
sudo modprobe dm_mod


### Install docker

## set up repository
sudo apt-get -y install \
	  apt-transport-https \
	    ca-certificates \
	      curl

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
	       "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
	              $(lsb_release -cs) \
		             stable"

sudo apt-get update

## Get Docker CE
sudo apt-get -y install docker-ce 

## Test
sudo docker run hello-world

sudo docker run -it ubuntu bash

sudo docker info 


