const express = require("express");
const utils = require("../utils");
const router = express.Router();

router.get("/:token", async (req, res, next) => {
	const request = await utils.server_query(`/verify/${req.params.token}`, "POST", {});
	res.send(`<h1> ${request.log} </h1>`);
});

module.exports = router;
