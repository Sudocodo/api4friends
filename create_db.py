from api import app, db
from models import UserModel, RecipeModel #Update for each new model

with app.app_context():
    db.create_all()