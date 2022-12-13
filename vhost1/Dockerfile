FROM ubuntu

RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
COPY sshd_config /etc/ssh/sshd_config
COPY ./credentials.csv /root/credentials.csv
ENV PULUMI_ACCESS_TOKEN="pul-YOUR_ACCESS_TOKEN"
ENV PATH="$PATH:/root/.pulumi/bin" 
# RUN apt install -y curl && apt install -y python3.10-venv && apt install -y unzip && apt install -y sudo
# RUN curl -fsSL https://get.pulumi.com | sh
# RUN pulumi login
# RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
# RUN unzip awscliv2.zip
# RUN sudo ./aws/install
# RUN aws configure import --csv file://credentials.csv
# RUN mkdir /opt/project_new && cd /opt/project_new && pulumi new aws-python --name misfaaaa --yes
COPY ./app.py /tmp/project_stuff/app.py
COPY ./sites.py /tmp/project_stuff/sites.py
COPY ./virtual_machines.py /tmp/project_stuff/virtual_machines.py
COPY ./templates /tmp/project_stuff/templates
COPY ./static /tmp/project_stuff/static
COPY ./requirements.txt tmp/project_stuff/requirements.txt
RUN echo 'root:123456' | chpasswd
CMD ["/usr/sbin/sshd", "-D"]

