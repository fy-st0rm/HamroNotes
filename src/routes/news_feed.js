const express = require("express");
const utils = require("../utils");
const router = express.Router();

router.post("/", async (req, res, next) => {
	let title = req.body.title;
	let category = req.body.category;
	let page = req.body.page;
	let amt = req.body.amt;

	let categories = await utils.fetch_categories();

	let payload = {
		"category_id": categories[category],
		"search_text": title,
		"page_no": page,
		"amount": amt
	};

	const request = await utils.server_query("/post_get", "POST", payload);
	res.json(request.ext);
});

module.exports = router;
