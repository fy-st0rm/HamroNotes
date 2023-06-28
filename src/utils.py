SUCESS = 200
FAILED = 400
TOKEN_EXIPRED = 401
NOT_FOUND = 404

def verify_key(keys: list, json: dict) -> bool:
	return all(k in json for k in keys)

