FROM registry.access.redhat.com/ubi8/ubi:latest
MAINTAINER Naing Ye Minn <naingyeminn@gmail.com>

WORKDIR /opt/app

RUN yum install -y --disableplugin=subscription-manager python3 python3-pip -y && yum clean all -y

ADD . /opt/app
RUN pip3 install -r requirements.txt

EXPOSE 8080

RUN chown -R 1001:1001 /opt/app
USER 1001

CMD ["python3", "app.py"]
