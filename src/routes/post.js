const express = require("express");
const auth = require("../auth");
const globals = require("../globals");
const router = express.Router();
const multer = require("multer");
const path = require("path");
const uuid = require("uuid");
const fs = require("fs");
const utils = require("../utils");

const storage = multer.diskStorage({
	destination: function(req, file, cb) {
		cb(null, globals.uploads_folder);
	},
	
	filename: function(req, file, cb) {
		cb(null, uuid.v4() + path.extname(file.originalname));
	}
});
let upload = multer({ storage: storage });

async function fetch_categories() {
	const response = await utils.server_query("/category", "GET", {});

	// TODO: This might explode. Be aware.
	let data = response.ext[0].categories;
	return data;
}

function init_folder(req, res, next) {
	if (!fs.existsSync(globals.uploads_folder)) {
		fs.mkdirSync(globals.uploads_folder);
	}
	next();
}

router.get("/", auth.auth_token, async (req, res, next) => {
	let categories = await fetch_categories();
	res.render("post", { categories: Object.keys(categories) } );
});

router.post("/", auth.auth_token, init_folder, upload.array("multi_images"), async (req, res, next) => {
	// TODO: Add field check
	let title = req.body.title;
	let description = req.body.description;
	let category = req.body.category;

	let categories = await fetch_categories();

	let file_names = [];
	for (let i = 0; i < req.files.length; i++) {
		file_names.push(req.files[i].filename);
	}

	let payload = {
		"title": title,
		"description": description,
		"content": file_names,
		"category": categories[category],
		"token": req.cookies.token
	};

	const request = await utils.server_query("/post", "POST", payload);
	console.log(request);

	res.redirect("home");
});

module.exports = router;
