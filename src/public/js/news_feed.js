import { server_ip, server_query, redirect_to } from "/js/utils.js";

const posts_list = document.querySelector('.posts');
let current_page = 1;
let amt = 3;

const fetch_post = async (page, amt) => {
	let payload = {
		"page": page,
		"amt": amt
	};
	const request = await server_query("/news_feed", "POST", payload);
	return request[0];
};

const add_click_event = (id) => {
	document.getElementById(`${id}`).addEventListener("click", () => {
		redirect_to(`/post/${id}`);
	});
};

const show_post = (posts) => {
	 posts.forEach(post => {
		const block = document.createElement('div');
		block.classList.add('post');
		block.setAttribute("id", `${post.id}`);
		block.innerHTML = `${post.title}`;
		posts_list.appendChild(block);

		add_click_event(post.id);
	});
};

const loader = async (page, amt) => {
	const posts = await fetch_post(page, amt);
	if (posts) {
		let values = Object.values(posts);
		show_post(values);
	}
};

window.addEventListener('scroll', () => {
	const {
		scrollTop,
		scrollHeight,
		clientHeight
	} = document.documentElement;

	if (scrollTop + clientHeight >= scrollHeight - 5) {
		current_page++;
		loader(current_page, amt);
	}
}, {
	passive: true
});

loader(current_page, amt);
