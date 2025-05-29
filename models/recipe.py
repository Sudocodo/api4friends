from models import db

class RecipeModel(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    cook_time = db.Column(db.Integer, nullable=False)
    prep_time = db.Column(db.Integer, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __init__(self, title, cook_time, prep_time, servings, description):
        self.title = title
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.servings = servings
        self.description = description

    def __repr__(self):
        return f'<Recipe(title={self.title})>'
