const express = require("express");
const url = require("url");
const globals = require("../globals");
const utils = require("../utils");

const router = express.Router();

router.get("/", (req, res, next) => {
	res.render("login", { result: req.query.result } );
});

router.post("/", async (req, res, next) => {
	let email    = req.body.email;
	let password = req.body.password;

	let payload = {
		"email": email,
		"password": password
	};

	let data = await utils.server_query("/login", "POST", payload);
	if (data.status == globals.FAILED) {
		res.render("login", { result: data.log });
		return;
	}

	let access_token = data.ext[0].token;
	res.header("Set-Cookie", [`token=${access_token}`, "secure", "httpOnly", "sameSite=Lax"]);
	res.redirect("/home");
});

module.exports = router;
