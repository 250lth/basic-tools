FROM ${docker.registry}/${docker.namespace}/python27:latest

MAINTAINER ${docker.maintainer}


# Install docker-ce
RUN yum -y install --setopt=tsflags=nodocs yum-utils device-mapper-persistent-data lvm2 && \
    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo && \
    yum makecache fast && \
    yum -y install --setopt=tsflags=nodocs docker-ce

# Add locales after locale-gen as needed
# Upgrade packages on image
# Preparations for sshd
RUN yum -y update --setopt=tsflags=nodocs && \
	yum -y install --setopt=tsflags=nodocs git && \
    yum -y install --setopt=tsflags=nodocs maven && \
    yum -y install --setopt=tsflags=nodocs sudo && \
    yum -y install --setopt=tsflags=nodocs openssh-server && \
    yum clean all && \
    ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''

# Install ansible
RUN pip install ansible

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

RUN echo "root:${docker.rootpwd}" | chpasswd

# Standard SSH port
EXPOSE 22

# Default command
CMD ["/usr/sbin/sshd", "-D"]
