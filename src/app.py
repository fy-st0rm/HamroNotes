from inc            import *
from model          import *


from routes.signup import signup
from routes.login import login
from routes.auth import auth
from routes.post import post
from routes.post import post_get
from routes.category import category
from routes.category import category_get
from routes.comment import comment

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
pdb.init_app(app)



# Routes
app.add_url_rule("/signup", view_func=signup, methods=["POST"])
app.add_url_rule("/login", view_func=login, methods=["POST"])
app.add_url_rule("/auth", view_func=auth, methods=["POST"])
app.add_url_rule("/post", view_func=post, methods=["POST"])
app.add_url_rule("/post/<id>", view_func=post_get, methods=["POST"])
app.add_url_rule("/category", view_func=category, methods=["POST"])
app.add_url_rule("/category_get", view_func=category_get, methods=["GET"])
app.add_url_rule("/comment", view_func=comment, methods=["POST"])

if __name__ == '__main__':
	app.run(debug=True)
