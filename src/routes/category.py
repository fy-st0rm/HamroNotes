from inc      import *
from model    import *
from response import *
from utils    import *

def category():
    response = request.get_json()
    if not verify_key(["title"], response):
        return Response(FAILED, "`title` are the required payload fields.", []).as_json()

    title = response['title']
    cat = Category(title=title)
    pdb.session.add(cat)
    pdb.session.commit()
    return Response(SUCESS, "Sucessfully Added Category.", []).as_json()