const express = require("express");
const auth    = require("../auth");
const utils  = require("../utils");
const router = express.Router();

router.get("/", auth.auth_token, async (req, res, next) => {
	let categories = await utils.fetch_categories();
	categories.all = null;
	res.render("home", { username: res.locals.username, categories: Object.keys(categories) });
});

module.exports = router;
