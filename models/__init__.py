from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
from .user import UserModel
from .recipe import RecipeModel
