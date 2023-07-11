from inc      import *
from model    import *
from response import *
from utils    import *
    


def comment():
    response = request.get_json()
    if not verify_key(["text", "post_id","token"], response):
        return Response(FAILED, "`text`, `post_id`,`token` are the required payload fields.", []).as_json()

    postId = response['post_id']
    text = response['text']
    token = response['token']

    try:
        decodedData = jwt.decode(jwt=token, key=os.getenv('SECRET_KEY'), algorithms=["HS256"])
    except jwt.exceptions.ExpiredSignatureError as e:
        return Response(TOKEN_EXIPRED, "Token has been expired.", []).as_json()
    except Exception as e:
        return Response(FAILED, "Token is invalid", []).as_json()
    id = decodedData['id']
    
    userQuery = User.query.filter_by(id=id).first()
    postQuery = User.query.filter_by(id=postId).first()

    if postQuery == None:
        return Response(FAILED, "Post Unavailable", []).as_json()
    
    pst = Comment(postId=postId, author=userQuery.id, text=text)
    pdb.session.add(pst)
    pdb.session.commit()
    return Response(SUCESS, "Sucessfully Added Comment.", []).as_json()
    

def comment_edit():
    response = request.get_json()
    if not verify_key(["text", "comment_id","token"], response):
        return Response(FAILED, "`text`, `comment_id`,`token` are the required payload fields.", []).as_json()

    commentId = response['comment_id']
    text = response['text']
    token = response['token']

    try:
        decodedData = jwt.decode(jwt=token, key=os.getenv('SECRET_KEY'), algorithms=["HS256"])
    except jwt.exceptions.ExpiredSignatureError as e:
        return Response(TOKEN_EXIPRED, "Token has been expired.", []).as_json()
    except Exception as e:
        return Response(FAILED, "Token is invalid", []).as_json()
    id = decodedData['id']

    commentQuery = Comment.query.filter_by(id=id).first()
    if commentQuery.id == id:
        commentQuery.text = text
        pdb.session.add(commentQuery)
        pdb.session.commit()
    return Response(SUCESS, "Sucessfully edited comment", []).as_json()
        

