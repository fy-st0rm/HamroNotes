from inc      import *
from model    import *
from response import *
from utils    import *
    


def post():
    response = request.get_json()
    if not verify_key(["title", "description", "content","category","token"], response):
        return Response(FAILED, "`title`, `description`,`content`,`category`,`token` are the required payload fields.", []).as_json()

    title = response['title']
    description = response['description']
    contents = response['content']
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

    pst = Post(title=title, description=description, category=category, author=userQuery.id)
    pdb.session.add(pst)
    pdb.session.commit()

    for content in contents:
        cont = Content(content=content, postId=pst.id)
        pdb.session.add(cont)
        pdb.session.commit()

    return Response(SUCESS, "Sucessfully Added Post.", []).as_json()

def post_get(id):
    postQuery = Post.query.filter_by(id=id).first()
    
    if postQuery == None:
        return Response(NOT_FOUND, "Unable To Find Post", []).as_json()
        
    userQuery = User.query.filter_by(id=postQuery.author).first()
    categoryQuery = Category.query.filter_by(id=postQuery.category).first()
    commentQuery  = Comment.query.filter_by(postId=postQuery.id).all()
    
    res = {
        "id": postQuery.id,
        "title":postQuery.title,
        "description": postQuery.description,
        "date":postQuery.date,
        "author": userQuery.username,
        "content": postQuery.content,
        "category": categoryQuery.title,
        "comments": []
    }

    for comment in commentQuery:
        userCommentQuery = User.query.filter_by(id=comment.author).first()
        comment_detail = {
            "id":comment.id,
            "upvoteCount":comment.upvoteCount,
            "solved":comment.solved,
            "text": comment.text,
            "author": userCommentQuery.username
        }
        res["comments"].append(comment_detail)

    return Response(SUCESS, "", [
        res
    ]).as_json()

    


