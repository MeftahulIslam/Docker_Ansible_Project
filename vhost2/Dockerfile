FROM ubuntu

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
COPY sshd_config /etc/ssh/sshd_config
RUN echo 'root:123456' | chpasswd
CMD ["/usr/sbin/sshd", "-D"]


