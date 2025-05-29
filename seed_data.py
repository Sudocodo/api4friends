from api import app, db
from models import UserModel, RecipeModel

users = [
    UserModel(name=f"User{i}", email=f"user{i}@example.com") for i in range(1, 11)
]

recipes = [
    RecipeModel(
        title=f"Test Recipe {i}",
        cook_time=10 + i,
        prep_time=5 + i,
        servings=2 + (i % 4),
        description=f"Delicious recipe number {i}."
    ) for i in range(1, 11)
]

with app.app_context():
    db.create_all()
    db.session.bulk_save_objects(users)
    db.session.bulk_save_objects(recipes)
    db.session.commit()
    print("Added 10 dummy users and 10 dummy recipes.")
