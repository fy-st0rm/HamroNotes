const express = require("express");
const auth    = require("../auth");
const router = express.Router();

router.get("/", auth.auth_token,  (req, res, next) => {
	res.render("home", { username: res.locals.username });
});

module.exports = router;
