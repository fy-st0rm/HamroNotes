const utils = require("./utils");
const url = require("url");
const globals = require("./globals");

exports.auth_token = async (req, res, next) => {
	let payload = {
		"token": req.cookies.token
	};

	let data = await utils.server_query("/auth", "POST", payload);

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
