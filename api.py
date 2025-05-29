from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from models import UserModel, RecipeModel, db
from routes.user_routes import Users, UsersAll
from routes.recipe_routes import Recipes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/db_4_friends'
db.init_app(app)
api = Api(app)

api.add_resource(Users, '/api/users/<int:user_id>')
api.add_resource(UsersAll, '/api/users/')
api.add_resource(Recipes, '/api/recipes/<int:recipe_id>', endpoint='recipe_by_id')
api.add_resource(Recipes, '/api/recipes/', endpoint='recipes_all')

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)