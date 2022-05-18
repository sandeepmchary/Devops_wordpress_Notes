//* to get the private ipv4 and host name of the server
const os = require('os');
const hostname = os.hostname();
const http = require('http');
console.log("nodejs server hostname: " + hostname);
var handler = function(request,response) {
    console.log("Received request from: " + request.connection.remoteAddress);
    response.writeHead(200);
    response.end("you've hit the server at " + hostname + " with ipv4: " + request.connection.remoteAddress);
    response
};
var www = http.createServer(handler);
www.listen(8080);