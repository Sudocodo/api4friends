from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/db_4_friends'
db = SQLAlchemy(app)
api = Api(app)

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User(name = {self.name}, email = {self.email})>'
    
user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help='Name of the user')
user_args.add_argument('email', type=str, required=True, help='Email of the user')

userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}

class Users(Resource):
    @marshal_with(userFields) #decorator to format the output
    def get(self, user_id):
        return UserModel.query.all()

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        new_user = UserModel(name=args['name'], email=args['email'])
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201

api.add_resource(Users, 'api/users/')

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201

    if request.method == 'GET':
        users = User.query.all()
        return {'users': [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]}

if __name__ == '__main__':
    app.run(debug=True)