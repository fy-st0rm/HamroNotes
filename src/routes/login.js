const express = require("express");
const url = require("url");
const fetch = require("node-fetch");
const globals = require("../globals");

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

	const request = await fetch(globals.server_ip + "/login", {
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
		res.redirect(url.format({
			pathname: "login",
			query: {
				"result": `${data.log}`
			}
		}));
		return;
	}

	let access_token = data.ext[0].token;
	res.header("Set-Cookie", [`token=${access_token}`, "secure", "httpOnly", "sameSite=Lax"]);
	res.redirect("/home");
});

module.exports = router;
