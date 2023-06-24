from inc      import *
from model    import *
from response import *
from utils    import *

def signup():
	response = request.get_json()

	if not verify_key(["email", "username", "password"], response):
		return Response(400, "`email`, `username`, `password` are the required payload fields.", []).as_json()
	
	email    = response['email']
	username = response['username']
	password = response['password']

	usrQuery = User.query.filter_by(email=email).first()

	if usrQuery:
		return Response(400,"Account already exists",[]).as_json()

	usr = User(email=email, password = password, username=username)
	pdb.session.add(usr)
	pdb.session.commit()

	return Response(200,"Sucessfully created account",[]).as_json()
