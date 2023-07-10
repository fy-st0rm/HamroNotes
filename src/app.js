// Dependencies
const express = require("express");
const path    = require("path");
const logger  = require("morgan");
const http    = require("http");
const multer  = require('multer');
const cookie_parser = require('cookie-parser');

// Routers
const index_router = require("./routes/index");
const signup_router = require("./routes/signup");
const login_router = require("./routes/login");
const home_router = require("./routes/home");
const error_router = require("./routes/error");
const logout_router = require("./routes/logout");
const post_router = require("./routes/post");
const image_router = require("./routes/image");
const comment_router = require("./routes/comment");
const verify_email_router = require("./routes/verify_email");

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
app.use(cookie_parser());
app.use(express.static(__dirname));

// Setting up routers
app.use("/", index_router);
app.use("/signup", signup_router);
app.use("/login", login_router);
app.use("/home", home_router);
app.use("/error", error_router);
app.use("/logout", logout_router);
app.use("/post", post_router);
app.use("/post", image_router);
app.use("/comment", comment_router);
app.use("/verify", verify_email_router);

// Running
const server = http.createServer(app);
server.listen(port);
