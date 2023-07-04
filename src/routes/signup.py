from inc      import *
from model    import *
from utils    import *
from hn_email import send_mail
from response import Response


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

	#send_mail(email, "Welcome to hm!","<h1>test</h1>")
	return Response(SUCESS,"Sucessfully created account",[]).as_json()
