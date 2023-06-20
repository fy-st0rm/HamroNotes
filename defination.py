from inc import *

'''
    This is where all the flask declarations are made
'''

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
CORS(app)
pdb = SQLAlchemy(app)
app.config['SECRET_KEY'] = '29bea2e273e64077a93ffb2d9ab3f7d0'




