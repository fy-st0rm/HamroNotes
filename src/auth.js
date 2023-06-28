const fetch = require("node-fetch");
const url = require("url");
const globals = require("./globals");

exports.auth_token = async (req, res, next) => {
	let payload = {
		"token": req.cookies.token
	};

	const request = await fetch(globals.server_ip + "/auth", {
		method: 'POST', 
		headers: {
			"Content-Type": "application/json",
			"Accept": "application/json"
		},
		body: JSON.stringify(payload)
	});

	let result = await request.text();
	let data = JSON.parse(result);

	// If authentication failed
	if (data.status == globals.FAILED) {
		res.redirect(url.format({
			pathname: "error",
			query: {
				"error": `${data.log}`
			}
		}));
		return;
	}
	else if (data.status == globals.TOKEN_EXPIRED) {
		res.redirect(url.format({
			pathname: "login",
			query: {
				"result": ``
			}
		}));
		return;
	}

	// Sucessfully authenticated
	let user = data.ext[0];
	res.locals.username = user.username;
	res.locals.email = user.email;

	next();
};
