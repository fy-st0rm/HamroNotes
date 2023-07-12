const fetch = require("node-fetch");
const globals = require("./globals");

async function server_query(endpoint, method, payload) {
	let params = {
		method: method,
		headers: {
			"Content-Type": "application/json",
			"Accept": "application/json"
		},
	};

	if (method != "GET") {
		params.body = JSON.stringify(payload);
	}

	const request = await fetch(globals.server_ip + endpoint, params);
	let result = await request.text();
	let data = JSON.parse(result);
	return data;
}

async function fetch_categories() {
	const response = await server_query("/category", "GET", {});

	// TODO: This might explode. Be aware.
	let data = response.ext[0].categories;
	data.all = null;
	return data;
}

exports.server_query = server_query;
exports.fetch_categories = fetch_categories;
