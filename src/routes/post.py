from inc      import *
from model    import *
from response import *
from utils    import *
    


def post():
    response = request.get_json()
    if not verify_key(["title", "discription", "content","category","token"], response):
        return Response(FAILED, "`title`, `discription`,`content`,`category`,`token` are the required payload fields.", []).as_json()

    title = response['title']
    discription = response['discription']
    content = response['content']
    category = response['category']
    token = response['token']
    
    try:
        decodedData = jwt.decode(jwt=token, key=os.getenv('SECRET_KEY'), algorithms=["HS256"])
    except jwt.exceptions.ExpiredSignatureError as e:
        return Response(TOKEN_EXIPRED, "Token has been expired.", []).as_json()
    except Exception as e:
        return Response(FAILED, "Token is invalid", []).as_json()

    id = decodedData['id']
    userQuery = User.query.filter_by(id=id).first()

    pst = Post(title=title, discription=discription, content=content, category=category, author=userQuery.id)
    pdb.session.add(pst)
    pdb.session.commit()
    return Response(SUCESS, "Sucessfully Added Post.", []).as_json()
    


