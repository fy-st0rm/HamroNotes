from inc import *
from model import *

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
				'expiration': str(datetime.utcnow() + timedelta(seconds=100)),
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
