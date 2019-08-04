
FROM ubuntu
MAINTAINER vamsi
RUN apt-get update && apt-get install -y gnupg2
RUN apt-get install default-jdk -y
RUN apt-get install wget -y
RUN wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | apt-key add -
RUN sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
RUN apt update && apt install jenkins -y 
RUN service jenkins start && sleep 20
RUN ["cat", "/var/lib/jenkins/secrets/initialAdminPassword"]
#RUN cat /var/lib/jenkins/secrets/initialAdminPassword
CMD service jenkins start && tail -f /dev/null








