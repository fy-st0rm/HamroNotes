from inc import *
from model import *
from response import *

def signup():
	response = request.get_json()
	
	email	 = response['email']
	username = response['username']
	password = response['password']
	usrQuery = User.query.filter_by(email=email).first()

	if usrQuery == None:
		usr = User(email=email, password = password, username=username)
		pdb.session.add(usr)
		pdb.session.commit()
		return Response(200,"Sucessfully created account",[]).as_json()
	else:
		return Response(400,"Account already exists",[]).as_json()
