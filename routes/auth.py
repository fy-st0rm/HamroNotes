from inc import *
from model import *

def token_required(func):
	@wraps(func)
	def decorated(*args, **kwargs):
		response = request.get_json()
		token = response['token']
		if not token:
			res = {"response": "token is missing"}
			return jsonify(res)
		try:
			payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
			return func(*args, **kwargs)
		except Exception as e:
			print(e)
			res = {"response": "token is invalid"}
			return jsonify(res)
	return decorated

@token_required
def auth():
	response = request.get_json()
	token = response['token']
	decodedData = jwt.decode(jwt=token, key=os.getenv('SECRET_KEY'), algorithms=["HS256"])
	print(decodedData)
	id = decodedData['id']
	usrQuery = usrQuery = User.query.filter_by(id=id).first()
	res = {
		"response":"Sucess",
		"username": usrQuery.username,
		"email": usrQuery.email
	}
	return jsonify(res)
