from inc   import *
from model import *
from utils import *
from response import *

def token_verification(func):
	@wraps(func)
	def decorated(*args, **kwargs):
		response = request.get_json()

		if not verify_key(["token"], response):
			return Response(FAILED, "`token` is the required payload fields.", []).as_json()

		token = response['token']
		if not token:
			return Response(FAILED, "`token` is empty.", []).as_json()

		try:
			payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=['HS256'])
			return func(*args, **kwargs)
		except jwt.exceptions.ExpiredSignatureError as e:
			return Response(TOKEN_EXIPRED, "Token has been expired.", []).as_json()
		except Exception as e:
			return Response(FAILED, "Token is invalid", []).as_json()

	return decorated

@token_verification
def auth():
	response = request.get_json()

	if not verify_key(["token"], response):
		return Response(FAILED, "`token` is the required payload fields.", []).as_json()

	token = response['token']

	decodedData = jwt.decode(jwt=token, key=os.getenv('SECRET_KEY'), algorithms=["HS256"])
	id = decodedData['id']

	usrQuery = User.query.filter_by(id=id).first()
	res = {
		"username": usrQuery.username,
		"email": usrQuery.email
	}
	return Response(SUCESS, "Token verified", [res]).as_json()
