# Version:0.0.1
FROM ubuntu:17.04
MAINTAINER Trevor Liu "gang250lth@gmail.com"
RUN apt-get update && apt-get install -y nginx
RUN echo 'Hi, I am your container' \
	> /usr/share/nginx/html/index.html 
EXPOSE 80
