FROM mysql:5.7.25
ENV MY_ROOT_PASSWORD="vprodbpass"
ENV MY_DATABASE="accounts"
ADD db_backup.sql /docker-entrypoint-initdb.d/db_backup.sql
# we need to add the db_backup.sql from
# https://github.com/devopshydclub/vprofile-project/tree/docker/src/main/resources
# db_backup.sql
# in the https://github.com/devopshydclub/vprofile-project
# branch docker
# cd src/main/resources
# we have application properties in src/main/resources
# in that we have jdbc.password as vprodbpass along with the database name as accounts
