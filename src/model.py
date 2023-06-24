from inc import * 

'''
	This is where the model of database is written
'''

pdb = SQLAlchemy()

class User(pdb.Model, UserMixin):
	id            = pdb.Column(pdb.Integer, primary_key=True)
	email         = pdb.Column(pdb.String(50))
	username      = pdb.Column(pdb.String(50))
	password_hash = pdb.Column(pdb.String(129))

	@property
	def password(self):
		raise AttributeError('you sneaky bastard!')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	
	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

