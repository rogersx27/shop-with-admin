FROM mysql:5.7

COPY ./conf.d /etc/mysql/conf.d

ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=sample_db
ENV MYSQL_USER=user
ENV MYSQL_PASSWORD=password

EXPOSE 3306

COPY ./initdb.d /docker-entrypoint-initdb.d
