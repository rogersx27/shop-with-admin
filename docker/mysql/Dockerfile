FROM mysql:8.0

ENV MYSQL_DATABASE=sample_db \
    MYSQL_USER=user \
    MYSQL_PASSWORD=password \
    MYSQL_ROOT_PASSWORD=password

COPY ./conf.d /etc/mysql/conf.d
COPY ./initdb.d /docker-entrypoint-initdb.d

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["mysqld"]
