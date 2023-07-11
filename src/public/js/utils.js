const server_ip = "http://localhost:3000";

const server_query = async (endpoint, method, payload) => {
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

	const request = await fetch(server_ip + endpoint, params);
	let result = await request.text();
	let data = JSON.parse(result);
	return data;
}

const redirect_to = async (endpoint) => {
	window.location.replace(server_ip + endpoint);
}

export { server_ip, server_query, redirect_to }
