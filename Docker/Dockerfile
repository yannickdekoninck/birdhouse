FROM arm32v7/python:3.9-buster

ENV CFLAGS=-fcommon
WORKDIR /usr/src/app

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y libatlas-base-dev

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


RUN apt-get install -y openssh-server sudo

RUN useradd -rm -d /home/birdmaster -s /bin/bash -g root -G sudo -u 1000 birdmaster

RUN usermod -aG sudo birdmaster

RUN  echo 'birdmaster:bluebird' | chpasswd

RUN service ssh start

EXPOSE 22

RUN export LD_LIBRARY_PATH=/opt/vc/lib


CMD ["/usr/sbin/sshd","-D"]
