from flask              import *
from flask_cors         import CORS
from flask_sqlalchemy   import SQLAlchemy
from werkzeug.security  import *
from flask_wtf          import *
from wtforms            import *
from wtforms.validators import *
from flask_login        import *
from datetime           import *
from functools          import wraps
import jwt

'''
    This is where all the flask imports are imported
'''