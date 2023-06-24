from inc            import *
from model          import *

from routes.signup import signup
from routes.login import login
from routes.auth import auth

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
pdb.init_app(app)

# Routes
app.add_url_rule("/signup", view_func=signup, methods=["POST"])
app.add_url_rule("/login", view_func=login, methods=["POST"])
app.add_url_rule("/auth", view_func=auth, methods=["POST"])

if __name__ == '__main__':
	app.run(debug=True)
