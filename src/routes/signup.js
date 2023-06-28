const express = require("express");
const url = require("url");
const fetch = require("node-fetch");
const globals = require("../globals");

const router = express.Router();

router.get("/", (req, res, next) => {
	res.render("signup", { result: req.query.result });
});

router.post("/", async (req, res, next) => {
	let email    = req.body.email;
	let username = req.body.username;
	let password = req.body.password;

	//TODO: Check for empty field and check for strong passwords

	let payload = {
		"email": email,
		"username": username,
		"password": password
	};

	const request = await fetch(globals.server_ip + "/signup", {
		method: 'POST', 
		headers: {
			"Content-Type": "application/json",
			"Accept": "application/json"
		},
		body: JSON.stringify(payload)
	});

	let result = await request.text();
	let data = JSON.parse(result);

	if (data.status == globals.FAILED) {
		res.render("signup", { result: data.log });
		return;
	}

	res.redirect(307, url.format({
		pathname: "login",
		query: {
			"email": email,
			"password": password,
			"result": ""
		}
	}));
});

module.exports = router;
