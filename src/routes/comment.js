const express = require("express");
const auth = require("../auth");
const utils = require("../utils");
const globals = require("../globals");
const router = express.Router();

router.post("/:post_id", auth.auth_token, async (req, res, next) => {
	let text = req.body.comment;
	let post_id = req.params.post_id;
	let token = req.cookies.token;

	let payload = {
		"text": text,
		"post_id": post_id,
		"token": token
	};

	const request = await utils.server_query("/comment", "POST", payload);
	if (request.status == globals.FAILED) {
		res.redirect(url.format({
			pathname: "../error",
			query: {
				"error": `${request.log}`
			}
		}));
		return;
	}

	res.redirect(`../post/${post_id}`);
});

module.exports = router;
