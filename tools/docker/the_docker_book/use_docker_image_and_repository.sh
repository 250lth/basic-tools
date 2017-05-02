### What is docker image

# formed by file systems:
# bootfs
# rootfs: ubuntu/debian
# union mount
# copy on write


### list images

## list
sudo docker images

## pull images
sudo docker pull ubuntu:17.04

## run a docker with tag
sudo docker run -it --name new_container ubuntu:17.04 bash


### pull images

## default pull latest
sudo docker run -it --name next_container ubuntu bash

## pull with tag
sudo docker pull fedora:20


### Search images

## use docker search to check from dockerhub
sudo docker search puppet

## pull 
sudo docker pull devopsil/puppet 

## create container
sudo docker run -it devopsil/puppet bash


### Build image

## login
sudo docker login

## create from commit
sudo docker run -it ubuntu bash 
apt-get -yqq update
apt-get -y install apache2
sudo docker commit fb73ef942c19 250lth/apache2

## add more data
sudo docker commit -m "A new custom image" -a "Trever Liu" fb73ef942c19 250lth/apache2:webserver

## check commited image
sudo docker inspect 250lth/apache2:webserver
