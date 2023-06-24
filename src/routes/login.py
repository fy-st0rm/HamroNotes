from inc import *
from model import *
from response import *

def login():
	response = request.get_json()
	email    = response['email']
	password = response['password']

	usrQuery = User.query.filter_by(email=email).first()

	if usrQuery == None:
		res = {"response": "Account Doesnt Exist"}
		return jsonify(res)
	else:
		if usrQuery.verify_password(password):
			session['logged_in'] = True
			token = jwt.encode({
				'email': email,
				'exp': datetime.utcnow() + timedelta(seconds=30),
				'id': usrQuery.id
			},
			os.getenv('SECRET_KEY'))

			res = {
				"response": "Sucessfully Logged In",
				"token": token
			}
		else:
			res = {"response":"Unable To Verify Check Your Password"}
		
		return jsonify(res)
