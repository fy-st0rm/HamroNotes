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

exports.server_query = server_query;
