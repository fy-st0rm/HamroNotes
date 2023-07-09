const express = require("express");
const globals = require("../globals");
const path = require("path");
const router = express.Router();

router.get("/image/:image_id", async (req, res, next) => {
	console.log(req.params.image_id);
	res.sendFile(path.resolve(globals.uploads_folder + req.params.image_id));
});

module.exports = router;
