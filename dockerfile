FROM centos7/python3_build as install
MAINTAINER linjinting

ARG PIP_MIRROR=https://pypi.douban.com/simple
ENV PIP_MIRROR=$PIP_MIRROR
WORKDIR /tmp

RUN rm -f /usr/bin/python \
    && ln -s /opt/python3/bin/python3 /usr/bin/python \
    && ln -s /opt/python3/bin/pip3 /usr/bin/pip \
    && sed -i 's@/usr/bin/python@/usr/bin/python2@g' /usr/bin/yum
    
COPY requirements.txt .
RUN pip install -r requirements.txt -i ${PIP_MIRROR}

FROM centos:centos7
MAINTAINER linjinting
WORKDIR /home/worker_query_py3

COPY --from=install /opt/python3 /opt/python3
COPY . .
RUN RUN localedef -c -f UTF-8 -i zh_CN zh_CN.UTF-8 \
    && export LC_ALL=zh_CN.UTF-8 \
    && echo 'LANG=zh_CN.UTF-8' > /etc/sysconfig/i18n \
    && \cp -f /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && rm -f /usr/bin/python \
    && ln -s /opt/python3/bin/python3 /usr/bin/python \
    && ln -s /opt/python3/bin/pip3 /usr/bin/pip \
    && sed -i 's@/usr/bin/python@/usr/bin/python2@g' /usr/bin/yum\
    && find /opt/python3 -depth \( \( -type d -a \( -name test -o -name tests -o -name idle_test \) \) -o \( -type f -a \( -name '*.pyc' -o -name '*.pyo' -o -name '*.a' \) \) -o \( -type f -a -name 'wininst-*.exe' \) \) -exec rm -rf '{}' \;
CMD ["sh", "celery_run.sh", "start"]