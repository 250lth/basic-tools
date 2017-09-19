#!/usr/bin/env bash


PROJECT_SETTINGS=${docker.project.path}/app/cms/settings.py
mkdir -p ${docker.spring.config.location}

CONF_FILE=${docker.spring.config.location}/settings.py
CONF_URL=${SPRING_CLOUD_CONFIG_URI}/${SPRING_CLOUD_CONFIG_NAME}/${SPRING_PROFILES_ACTIVE}/${SPRING_CLOUD_CONFIG_LABEL}/${SPRING_CLOUD_CONFIG_NAME}-${SPRING_PROFILES_ACTIVE}.txt
rm -f ${CONF_FILE}
rm -f ${PROJECT_SETTINGS}

STATUS=$(curl -I -u ${SPRING_CLOUD_CONFIG_USERNAM}:${SPRING_CLOUD_CONFIG_PASSWORD} ${CONF_URL}|head -n 1|cut -d$' ' -f2)
if [[ "${STATUS}" != "200" ]]; then
  echo "config file is not available: ${CONF_URL}"
  tailf /dev/null
  exit 1
fi

curl -o ${CONF_FILE} -u ${SPRING_CLOUD_CONFIG_USERNAM}:${SPRING_CLOUD_CONFIG_PASSWORD} ${CONF_URL}
if [[ $? -ne 0 ]]; then
  echo "fetch config file fail: ${CONF_URL}"
  tailf /dev/null
  exit 1
fi

ln -s ${CONF_FILE} ${PROJECT_SETTINGS}


mkdir -p /data/logs/webapps/${docker.project.name}
sed -i -e 's!/var/run/supervisor/supervisor.sock!/dev/shm/supervisor.sock!' /etc/supervisord.conf
supervisord -n