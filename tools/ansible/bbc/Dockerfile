FROM registry.cn-shenzhen.aliyuncs.com/allwinner/python27:latest

MAINTAINER ${docker.maintainer}

# Add locales after locale-gen as needed
# Upgrade packages on image
# Preparations for sshd
RUN yum -y update --setopt=tsflags=nodocs && \
    yum -y install --setopt=tsflags=nodocs git && \
    yum -y install --setopt=tsflags=nodocs maven && \
    yum -y install --setopt=tsflags=nodocs sudo && \
    yum -y install --setopt=tsflags=nodocs openssh-server && \
    yum -y install --setopt=tsflags=nodocs openssh-clients && \
    yum -y install --setopt=tsflags=nodocs openssl && \
    yum -y install --setopt=tsflags=nodocs sshpass && \
    yum clean all 

# Install ansible
RUN pip install --upgrade pip 
RUN pip install ansible

# Generate ssh host key
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN echo "root:${docker.rootpwd}" | chpasswd

# Standard SSH port
EXPOSE 22

# Default command
# Run ssh server 
CMD ["/usr/sbin/sshd", "-D"]
