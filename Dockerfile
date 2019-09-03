FROM python:3

# Docker Variables
MAINTAINER Jinchi Zhang <jizjiz148148@gmail.com>
LABEL maintainer="jizjiz148148@gmail.com"
LABEL organization="RiftBorn"
LABEL project="rift-projects"

# Setup system & packages
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    bash \
    ca-certificates \
    curl \
    groff \
    jq \
    less \
    make \
    nano \
    tree \
    tar \
    wget \
    zip \
 && rm -rf /var/lib/apt/lists/* \
 && rm /bin/sh && ln -sf /bin/bash /bin/sh \
 && echo "export PS1='\n\u@\h [\w] \D{%F %T} [\#]:\n\$ '" >> ~/.bashrc \
 && echo "alias ll='ls -al'" >> ~/.bashrc \
 && echo "" >> ~/.bashrc

COPY tools/entrypoint.sh /usr/local/bin/entrypoint.sh

# Project Variables
ENV PROJECT=rift-projects \
    PROJECT_DIR=interview \
    SHELL=/bin/bash \
    SOURCE=/src

COPY $PROJECT_DIR/requirements-dev.txt $SOURCE/$PROJECT/requirements-dev.txt
COPY $PROJECT_DIR/requirements.txt $SOURCE/$PROJECT/requirements.txt

# install python dependencies, and aws cli
RUN mkdir -p $SOURCE \
 && pip install --upgrade pip \
#&& pip install -r $SOURCE/$PROJECT/requirements-dev.txt \
#&& pip install -r $SOURCE/$PROJECT/requirements.txt \
 && pip install awscli

WORKDIR $SOURCE/$PROJECT

# ENTRYPOINT ["/bin/bash", "-c"]
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

CMD ["/bin/bash"]
