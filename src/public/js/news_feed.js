import { server_ip, server_query, redirect_to } from "/js/utils.js";

const posts_list = document.querySelector('.posts');
const search_form = document.querySelector('.search');

class NewsFeed {
	constructor() {
		this.current_page = 1;
		this.post_amount = 3;

		this.search_text = null;
		this.search_category = document.getElementById("category").value;
	}

	async fetch_post (title, category, page, amt) {
		let payload = {
			"title": title,
			"category": category,
			"page": page,
			"amt": amt
		};
		const request = await server_query("/news_feed", "POST", payload);
		return request[0];
	};

	add_click_event(id) {
		document.getElementById(`${id}`).addEventListener("click", () => {
			redirect_to(`/post/${id}`);
		});
	};

	show_post(posts) {
		 posts.forEach(post => {
			const block = document.createElement('div');
			block.classList.add('post');
			block.setAttribute("id", `${post.id}`);
			block.innerHTML = `${post.title}`;
			posts_list.appendChild(block);
	
			this.add_click_event(post.id);
		});
	};

	async reload() {
		const posts = await this.fetch_post(this.search_text, this.search_category, this.current_page, this.post_amount);
		if (posts) {
			let values = Object.values(posts);
			this.show_post(values);
		}
	};
};

const news_feed = new NewsFeed();
news_feed.reload();

search_form.addEventListener("submit", () => {
	let form_title = document.getElementById("title").value;
	let form_category = document.getElementById("category").value;

	news_feed.search_text = form_title ? form_title : null;
	news_feed.search_category = form_category;

	document.getElementsByClassName("posts")[0].innerHTML = "";
	news_feed.current_page = 1;
	news_feed.reload();
});

window.addEventListener('scroll', () => {
	const {
		scrollTop,
		scrollHeight,
		clientHeight
	} = document.documentElement;

	if (scrollTop + clientHeight >= scrollHeight - 5) {
		news_feed.current_page++;
		news_feed.reload();
	}
}, {
	passive: true
});

