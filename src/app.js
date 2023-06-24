// Dependencies
const express = require("express");
const path    = require("path");
const logger  = require("morgan");
const http    = require("http");

// Routers
const index_router = require("./routes/index");
const signup_router = require("./routes/signup");

// Express app
const app = express();
const port = 3000;

// Setting up view engine
app.use(logger('dev'));
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");
app.set("port", port);

// Setting up application settings
app.use(express.json());
app.use(express.urlencoded({ extended: false }));

// Setting up routers
app.use("/", index_router);
app.use("/signup", signup_router);

// Running
const server = http.createServer(app);
server.listen(port);
