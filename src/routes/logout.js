const express = require("express");
const url = require("url");
const router = express.Router();

router.post("/", (req, res, next) => {
	res.clearCookie("token");
	res.clearCookie("sameSite");

	res.redirect(url.format({
		pathname: "login"
	}));
});

module.exports = router;
