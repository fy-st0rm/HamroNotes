
def verify_key(keys: list, json: dict) -> bool:
	return all(k in json for k in keys)

