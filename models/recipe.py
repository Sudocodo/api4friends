from models import db

class RecipeModel(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    cook_time = db.Column(db.Integer, nullable=True)
    prep_time = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text, nullable=True)
    calories = db.Column(db.Integer, nullable=True)
    servings = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now(), nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)
    is_private = db.Column(db.Boolean, default=True, nullable=False)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, title, cook_time, prep_time, servings, description, created_by, calories=None, is_private=False):
        self.title = title
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.servings = servings
        self.description = description
        self.created_by = created_by
        self.calories = calories
        self.is_private = is_private

    def __repr__(self):
        return f'<Recipe(title={self.title}, created_by={self.created_by})>'
