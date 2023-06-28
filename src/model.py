from inc import * 

'''
	This is where the model of database is written
'''

pdb = SQLAlchemy()

	
class User(pdb.Model, UserMixin):
	id            = pdb.Column(pdb.Integer, primary_key=True)
	email         = pdb.Column(pdb.String(50))
	username      = pdb.Column(pdb.String(50))
	password_hash = pdb.Column(pdb.String(250))
	password_salt = pdb.Column(pdb.String(100))

	@property
	def password(self):
		raise AttributeError('you sneaky bastard!')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password + self.password_salt)
	
	

class Category(pdb.Model):
	id = pdb.Column(pdb.Integer, primary_key=True)
	title  = pdb.Column(pdb.String(50))

class Post(pdb.Model):
	id = pdb.Column(pdb.Integer, primary_key=True)
	title  = pdb.Column(pdb.String(50))
	discription = pdb.Column(pdb.String(150))
	date = pdb.Column(pdb.DateTime, default=datetime.datetime.utcnow)
	content = pdb.Column(pdb.String(10000))
	category = pdb.Column(pdb.Integer, pdb.ForeignKey(Category.id))
	author = pdb.Column(pdb.Integer, pdb.ForeignKey(User.id))


class Comment(pdb.Model):
	id = pdb.Column(pdb.Integer, primary_key=True)
	upvoteCount = pdb.Column(pdb.Integer)
	solved = pdb.Column(pdb.Boolean, default=False)
	text = pdb.Column(pdb.String(150))
	postId = pdb.Column(pdb.Integer, pdb.ForeignKey(Post.id))
	author = pdb.Column(pdb.Integer, pdb.ForeignKey(User.id))






	




