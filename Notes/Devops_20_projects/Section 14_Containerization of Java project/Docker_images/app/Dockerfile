FROM tomcat:8-jre11
# Remove the default Tomcat welcome page
RUN rm -rf /usr/local/tomcat/webapps/*
# Copy the application to the Tomcat webapps directory
COPY target/vprofile-v2.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
CMD [ "catalina.sh", "run" ]
WORKDIR /usr/local/tomcat
VOLUME /usr/local/tomcat/webapps
