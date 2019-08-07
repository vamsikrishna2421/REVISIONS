FROM ubuntu
MAINTAINER vamsi
RUN apt-get update
RUN apt-get install default-jdk -y
RUN apt-get install wget -y
RUN wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
RUN sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
RUN apt update && apt install -y jenkins
CMD service jenkins start
