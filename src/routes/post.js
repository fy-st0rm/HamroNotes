const express = require("express");
const auth = require("../auth");
const globals = require("../globals");
const router = express.Router();
const multer = require("multer");
const path = require("path");
const uuid = require("uuid");
const fs = require("fs");
const utils = require("../utils");
const url = require("url");

const storage = multer.diskStorage({
	destination: function(req, file, cb) {
		cb(null, globals.uploads_folder);
	},
	
	filename: function(req, file, cb) {
		cb(null, uuid.v4() + path.extname(file.originalname));
	}
});
let upload = multer({ storage: storage });

function init_folder(req, res, next) {
	if (!fs.existsSync(globals.uploads_folder)) {
		fs.mkdirSync(globals.uploads_folder);
	}
	next();
}

router.get("/", auth.auth_token, async (req, res, next) => {
	let categories = await utils.fetch_categories();
	res.render("post", { categories: Object.keys(categories) } );
});

router.post("/", auth.auth_token, init_folder, upload.array("multi_images"), async (req, res, next) => {
	// TODO: Add field check
	let title = req.body.title;
	let description = req.body.description;
	let category = req.body.category;

	let categories = await utils.fetch_categories();

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
	if (request.status == globals.FAILED) {
		res.redirect(url.format({
			pathname: "../error",
			query: {
				"error": `${request.log}`
			}
		}));
		return;
	}

	res.redirect("home");
});

router.get("/:post_id", async (req, res, next) => {
	let post_id = req.params.post_id;

	const request = await utils.server_query(`/post/${post_id}`, "POST");

	if (request.status == globals.NOT_FOUND || request.status == globals.FAILED) {
		res.redirect(url.format({
			pathname: "../error",
			query: {
				"error": `${request.log}`
			}
		}));
		return;
	}

	let post = request.ext[0];
	res.render("post_viewer", {
		id: post.id,
		title: post.title,
		author: post.author,
		date: post.date,
		description: post.description,
		content: post.content,
		comment: post.comments
	});
});

module.exports = router;
