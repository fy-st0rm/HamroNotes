const express = require("express");
const router = express.Router();
const url = require("url");
const fetch = require("node-fetch");
const globals = require("../globals");

router.get("/", (req, res, next) => {
	res.render("signup", { result: req.query.result });
});

router.post("/", async (req, res, next) => {
	let email    = req.body.email;
	let username = req.body.username;
	let password = req.body.password;

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

	res.redirect(url.format({
		pathname: "signup",
		query: {
			"result": `${data.log}`
		}
	}));
});

module.exports = router;
