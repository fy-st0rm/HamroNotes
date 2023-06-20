from inc            import *
from defination     import *
from model          import *

'''
    This is where you write views for different pages
'''

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        response = request.get_json()
        token = response['token']
        if not token:
            res = {"response": "token is missing"}

            return jsonify(res)
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            return func(*args, **kwargs)
        except Exception as e:
            res = {"response": "token is invalid"}
            return jsonify(res)
    return decorated

        

@app.route('/signup',methods=['POST'])
def signup():

    response = request.get_json()
    email = response['email']
    username = response['username']
    password = response['password']
    usrQuery = user.query.filter_by(email=email).first()

    if usrQuery == None:

        usr = user(email=email, password = password, username=username)
        pdb.session.add(usr)
        pdb.session.commit()

        res = {"response": "Sucessfully Created Account"}
        return jsonify(res)
    else:
        res = {"response": "Email Is Already Used"}
        return jsonify(res)

@app.route('/login',methods=['POST'])
def login():
    response = request.get_json()
    email = response['email']
    password = response['password']

    usrQuery = user.query.filter_by(email=email).first()

    if usrQuery == None:
        res = {"response": "Account Doesnt Exist"}

        return jsonify(res)
    else:
        
        if usrQuery.verify_password(password):
           session['logged_in'] = True
           token = jwt.encode(
               {
                   'email': email,
                   'expiration': str(datetime.utcnow() + timedelta(seconds=100)),
                   'id': usrQuery.id
                },
            app.config['SECRET_KEY'])
           
           res = {
               "response": "Sucessfully Logged In",
               "token": token
            }
           
        else:
            res = {"response":"Unable To Verify Check Your Password"}
        
        
        return jsonify(res)

@app.route('/',methods=['POST'])
def home():
    if session.get('logged_in'):
        res = {"response": "Sucessfully Logged In"}
        return jsonify(res)
    else:
        res = {"response": "Not Logged Int"}
        return jsonify(res)


@app.route('/auth', methods=["POST"])
@token_required
def auth():
    response = request.get_json()
    token = response['token']
    decodedData = jwt.decode(jwt=token, key=app.config['SECRET_KEY'], algorithms=["HS256"])
    print(decodedData)
    id = decodedData['id']
    usrQuery = usrQuery = user.query.filter_by(id=id).first()
    res = {"response":"Sucess",
           "username": usrQuery.username,
           "email": usrQuery.email
           }
    return jsonify(res)
    

