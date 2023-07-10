from inc      import *
from model    import *
from utils    import *
from hn_email import send_mail
from response import Response
from verification_template import *


def signup():
	response = request.get_json()

	if not verify_key(["email", "username", "password"], response):
		return Response(FAILED, "`email`, `username`, `password` are the required payload fields.", []).as_json()
	
	email    = response['email']
	username = response['username']
	password = response['password']

	usrQuery = User.query.filter_by(email=email).first()

	if usrQuery:
		return Response(FAILED,"Account already exists",[]).as_json()

	salt = str(secrets.token_hex(32))
	password = password + salt
	usr = User(email=email, password = password, username=username, password_salt = salt)
	pdb.session.add(usr)
	pdb.session.commit()

	token = jwt.encode({
		'email': email,
		'exp': datetime.datetime.utcnow() + timedelta(minutes=30),
	},
	os.getenv('SECRET_KEY'))
	link = "http://127.0.0.1:3000/verify/" + token
	send_mail(email, SUBJECT ,get_email_template(link))
	return Response(SUCESS,"Sucessfully created account",[]).as_json()
