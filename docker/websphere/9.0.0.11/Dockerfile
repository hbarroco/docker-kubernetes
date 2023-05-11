FROM ibmcom/websphere-traditional:9.0.0.11

LABEL MAINTAINER='Helio Barroco <heliobarroco@gmail.com>'

ARG PROFILE_NAME=AppSrv01
ARG CELL_NAME=localhostNode01Cell
ARG NODE_NAME=node01
ARG HOST_NAME=localhost
ARG SERVER_NAME=server1
ENV WAS_HOME /opt/IBM/WebSphere/AppServer/
ENV WAS_HOME_PROFILES /opt/IBM/WebSphere/AppServer/profiles

#Default ports
ARG HTTP_PORT=9080
ARG HTTPS_PORT=9043
ARG CONSOLE_PORT=9060

ENV PROFILE_NAME=$PROFILE_NAME \
  SERVER_NAME=$SERVER_NAME \
  HOST_NAME=$HOST_NAME
  
ENV HTTP_PORT=${HTTP_PORT}
ENV HTTPS_PORT=${HTTPS_PORT}
ENV CONSOLE_PORT=${CONSOLE_PORT}
#ENV HTTP_PORT="\${HTTP_PORT}"
#ENV HTTPS_PORT="\${HTTPS_PORT}"
#ENV CONSOLE_PORT="\${CONSOLE_PORT}"

RUN echo " <<<<<< Setting user root >>>>>> "
USER root

RUN echo " <<<<<< Apt-Gets >>>>>> "
RUN apt-get update && apt-get install sudo && rm -rf /var/lib/apt/lists/* 

RUN echo " <<<<<< Creating folders >>>>>> "
RUN mkdir -p /home/developer

RUN echo " <<<<<< Settings to developer user >>>>>> "
RUN export uid=1000 gid=1000 && \ 
  echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
  echo "developer:x:${uid}:" >> /etc/group && \
  echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
  chmod 0440 /etc/sudoers.d/developer && \
  chown ${uid}:${gid} -R /home/developer && \
  chown developer /opt && \
  chown -R developer:developer $WAS_HOME

RUN echo " <<<<<< Copy files hosto to containeir >>>>>> "
COPY ./utils/Password /tmp/PASSWORD
COPY ./utils/configWebSphere9.py /work/config
COPY ./utils/changeDefaultPorts.sh /usr/bin/changeDefaultPorts.sh
COPY ./utils/deploy.py /usr/bin/
COPY ./utils/pyLibs /usr/lib/pyLibs
#COPY trust.p12 /opt/IBM/WebSphere/AppServer/profiles/default/etc

RUN echo " <<<<<< Enable to change default ports >>>>>> "
RUN sed -i 's/trusthostheaderport = true/com.ibm.ws.webcontainer.extractHostHeaderPort = true/g' $WAS_HOME/profiles/$PROFILE_NAME/properties/soap.client.props

RUN echo " <<<<<< Run changeDefaultPorts.sh websphere >>>>>> "
RUN chmod +x /usr/bin/changeDefaultPorts.sh
RUN /usr/bin/changeDefaultPorts.sh

RUN echo " <<<<<< Run configure.sh websphere >>>>>> "
RUN /work/configure.sh
