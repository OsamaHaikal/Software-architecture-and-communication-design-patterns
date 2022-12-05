/* Client Code 

let sse = new EventSource("http://localhost:8080/stream");
sse.onmessage = console.log

*/

const app = require("express")();
// Add headers before the routes are defined
app.use(function (req, res, next) {

    // Website you wish to allow to connect
    res.setHeader("Access-Control-Allow-Origin", "http://localhost:5500");

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', true);

    // Pass to next layer of middleware
    next();
});

app.get("/", (req, res) => res.send("hello!"));

app.get("/stream", (req,res) => {

    res.setHeader("Content-Type", "text/event-stream");
    send(res);

})

const port = 8080;

let i = 0;

function send (res) {
    res.write("data: " + `hello from server ---- [${i++}]\n\n`);
    setTimeout(() => send(res), 500);
}

app.listen(port)

console.log(`Listening on ${port}`)