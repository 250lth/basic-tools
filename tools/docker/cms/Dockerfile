FROM ${docker.registry}/${docker.namespace}/python27:latest

MAINTAINER ${docker.maintainer}


COPY ./${docker.project.name}.tar.gz /tmp/

RUN mkdir -p ${docker.project.path}/app && \
    tar -xzf /tmp/${docker.project.name}.tar.gz -C /${docker.project.path}/app/ && \
    rm -f /tmp/${docker.project.name}.tar.gz && \
    virtualenv ${docker.project.path}/env

COPY ./supervisor-app.ini /etc/supervisord.d/
COPY ./nginx-webapp.conf /etc/nginx/conf.d/
COPY ./uwsgi.ini ${docker.project.path}/env/
COPY ./docker-entrypoint.sh /docker-entrypoint.sh
COPY ./build.meta /

RUN chmod ug+x /docker-entrypoint.sh && \
    source ${docker.project.path}/env/bin/activate && \
    pip install -r ${docker.project.path}/app/requirements.txt && \
    python ${docker.project.path}/app/manage.py collectstatic --noinput && \
    deactivate


EXPOSE ${docker.server.port}

ENTRYPOINT ["/bin/bash", "-c", "/docker-entrypoint.sh"]
