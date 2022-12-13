FROM ubuntu

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
COPY sshd_config /etc/ssh/sshd_config
COPY ./database.sql /tmp/database.sql
COPY ./mysqld.cnf /tmp/mysqld.cnf
RUN echo 'root:123456' | chpasswd
CMD ["/usr/sbin/sshd", "-D"]

