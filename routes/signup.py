from inc import *
from model import *

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

		res = {"response": "Sucessfully Created Account"}
		return jsonify(res)
	else:
		res = {"response": "Email Is Already Used"}
		return jsonify(res)
