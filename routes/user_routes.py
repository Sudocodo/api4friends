from flask_restful import Resource, reqparse, fields, marshal_with
from models import UserModel, db

user_args = reqparse.RequestParser()
user_args.add_argument('name', type=str, required=True, help='Name of the user')
user_args.add_argument('email', type=str, required=True, help='Email of the user')

userFields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String
}

class Users(Resource):
    @marshal_with(userFields)
    def get(self, user_id=None):
        if (user_id is not None):
            user = UserModel.query.filter_by(id=user_id).first()
            if not user:
                return {'message': 'User not found'}, 404
            return user
        return {'message': 'User ID required'}, 400

    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        new_user = UserModel(name=args['name'], email=args['email'])
        db.session.add(new_user)
        db.session.commit()
        return new_user, 201

class UsersAll(Resource):
    @marshal_with(userFields)
    def get(self):
        return UserModel.query.all()
