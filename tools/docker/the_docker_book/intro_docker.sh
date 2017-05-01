### ensure docker is all set
sudo docker info 


### run the first docker
sudo docker run -it ubuntu bash


### use the first docker

## check hostname
hostname

## check hosts
cat /etc/hosts 

## check interfaces
ip a 

## check processes
ps -aux

## install software
apt-get update && apt-get install vim

## list docker
sudo docker ps


### name docker
sudo docker run --name bob_the_container -it ubuntu bash 


### restart docker 

## start the exited docker
sudo docker start bob_the_container
# we can use id instead


### Reuse docker
sudo docker attach bob_the_container 


### create daemonized container

## create 
sudo docker run --name daemon_dave -d ubuntu bash -c "while true; do echo hello world; sleep 1; done"

## check 
sudo docker ps 


### What are doing inside dockers

## get daemon log
sudo docker logs daemon_dave 

## track daemon log
sudo docker logs -f daemon_dave 

## add time stamp
sudo docker logs -ft daemon_dave 


### Docker log driver

## start Syslog in docker
sudo docker run --log-driver="syslog" --name daemon_dwayne -d ubuntu bash -c "while true; do echo hello world; sleep 1; done"


### Check processes in docker

## check daemon
sudo docker top daemon_dave


### Docker statistic
sudo docker stats daemon_dave daemon_kate daemon_clare daemon_sarah


### run process in docker

## run back groud command
sudo docker exec -d daemon_dave touch /etc/new_config_file

## run interactive command
sudo docker exec -t -i daemon_dave bash

