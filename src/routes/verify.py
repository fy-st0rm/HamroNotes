from inc	  import *
from model	  import *
from response import *
from utils	  import *
	


def verify(token):
	response = request.get_json()
	
	try:
		decodedData = jwt.decode(jwt=token, key=os.getenv('SECRET_KEY'), algorithms=["HS256"])
	except jwt.exceptions.ExpiredSignatureError as e:
		return Response(TOKEN_EXIPRED, "Token has been expired.", []).as_json()
	except Exception as e:
		app.logger.debug(e)
		return Response(FAILED, "Token is invalid", []).as_json()
	email = decodedData['email']
	userQuery = User.query.filter_by(email=email).first()
	userQuery.isVerified = True
	pdb.session.add(userQuery)
	pdb.session.commit()
	return Response(SUCESS, "Sucessfully Verified Email", []).as_json()
