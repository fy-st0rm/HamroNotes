from inc      import *
from model    import *
from response import *
from utils    import *
    


def post():
    response = request.get_json()
    if not verify_key(["title", "discription", "content","category","token"], response):
        return Response(400, "`title`, `discription`,`content`,`category`,`token` are the required payload fields.", []).as_json()

    title = response['title']
    discription = response['discription']
    content = response['content']
    category = response['category']
    token = response['token']

    decodedData = jwt.decode(jwt=token, key=os.getenv('SECRET_KEY'), algorithms=["HS256"])
    id = decodedData['id']
    userQuery = User.query.filter_by(id=id).first()

    pst = Post(title=title, discription=discription, content=content, category=category, author=userQuery.id)
    pdb.session.add(pst)
    pdb.session.commit()
    return Response(200, "Sucessfully Added Post.", []).as_json()
    


