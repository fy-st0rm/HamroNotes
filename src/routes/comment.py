from inc      import *
from model    import *
from response import *
from utils    import *
    


def comment():
    response = request.get_json()
    if not verify_key(["text", "post_id","token"], response):
        return Response(400, "`text`, `post_id`,`token` are the required payload fields.", []).as_json()

    postId = response['post_id']
    text = response['text']
    token = response['token']

    decodedData = jwt.decode(jwt=token, key=os.getenv('SECRET_KEY'), algorithms=["HS256"])
    id = decodedData['id']
    
    userQuery = User.query.filter_by(id=id).first()
    postQuery = User.query.filter_by(id=postId).first()

    if postQuery == None:
        return Response(400, "Post Unavailable", []).as_json()
    
    pst = Comment(postId=postId, author=userQuery.id, text=text)
    pdb.session.add(pst)
    pdb.session.commit()
    return Response(200, "Sucessfully Added Comment.", []).as_json()
    


