FROM debian

RUN apt update && apt install -y openssh-server
RUN mkdir /var/run/sshd
COPY sshd_config /etc/ssh/sshd_config
RUN echo 'root:123456' | chpasswd
COPY ./server.py /tmp/server.py
CMD ["/usr/sbin/sshd", "-D"]

