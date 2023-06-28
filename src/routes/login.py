from inc      import *
from model    import *
from response import *
from utils    import *

def login():
	response = request.get_json()

	if not verify_key(["email", "password"], response):
		return Response(FAILED, "`email`, `password` are the required payload fields.", []).as_json()

	email    = response['email']
	password = response['password']

	usrQuery = User.query.filter_by(email=email).first()

	if usrQuery == None:
		return Response(FAILED, f"Account with email `{email}` doesnt exists.", []).as_json()

	if not usrQuery.verify_password(password):
		return Response(FAILED, "Unable To Verify. Check Your Password", []).as_json()

	session['logged_in'] = True
	token = jwt.encode({
		'email': email,
		'exp': datetime.datetime.utcnow() + timedelta(days=30),
		'id': usrQuery.id
	},
	os.getenv('SECRET_KEY'))

	return Response(SUCESS, "Sucessfully Logged In.", [{"token": token}]).as_json()
