<pre>
# HOW-DOCKERIZE-NODE-APPLICATION
                                  ## MANUAL STEPS
    * $ yum install nodejs -y
    * $ mkdir helloworld (create a folder)
    * $ cd helloworld
    * $ npm init
    * When asked for the details of the application (name, version, etc.), just confirm the default values with enter
    * Npm will create a package.json that will hold the dependencies of the app. Let’s add the Express Framework as the first dependency
    * $ npm install express --save
    * $ vi index.js
//Load express module with `require` directive
var express = require('express')
var app = express()

//Define request response in root URL (/)
app.get('/', function (req, res) {
  res.send('Hello World!')
})

//Launch listening server on port 8081
app.listen(8081, function () {
  console.log('app listening on port 8081!')
})
    * Run the app
    * $ node index.js
    * Go to http://localhost:8081/ in your browser to view it.
    --------------------------------------------------------------------------------------------------------------------------
    Dockerizing Node.js application
    * copy package.json and index.js to the present working directory
    * vi Dockerfile // pollute these with below
FROM node:7
WORKDIR /app
COPY package.json /app
RUN npm install
COPY . /app
CMD node index.js
EXPOSE 8081
    
    * Build Docker image
    * $ docker build -t hello-world .
    * Run Docker container
    * $ docker run -p 8081:8081 hello-world
    * Sharing Docker image
    * Sign up at hub.docker.com
    *  $ docker build -t [USERNAME/USER ID]/hello-world .
    *  $ docker login
    *  $ docker push [USERNAME]/hello-world
    * ANY SERVER USE THIS AS $ docker run [USERNAME]/hello-world
    *** sudo docker run -d -p 8080(EXTERNAL FOR HOST SYSTEM):8081(INTERNAL IN THE DOCKER FILE) formycore/helloworld 



</pre>