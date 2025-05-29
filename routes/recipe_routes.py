from flask_restful import Resource, reqparse, fields, marshal_with
from models import RecipeModel, db

recipe_args = reqparse.RequestParser()
recipe_args.add_argument('title', type=str, required=True, help='Title of the recipe')

recipeFields = {
    'id': fields.Integer,
    'title': fields.String,
    'cook_time': fields.Integer,
    'prep_time': fields.Integer,
    'servings': fields.Integer,
    'description': fields.String
}

class Recipes(Resource):
    @marshal_with(recipeFields)
    def get(self, recipe_id=None):
        if recipe_id is not None:
            recipe = RecipeModel.query.filter_by(id=recipe_id).first()
            if not recipe:
                return {'message': 'Recipe not found'}, 404
            return recipe
        return RecipeModel.query.all()

    @marshal_with(recipeFields)
    def post(self):
        args = recipe_args.parse_args()
        new_recipe = RecipeModel(
            title=args['title'],
            cook_time=args['cook_time'],
            prep_time=args['prep_time'],
            servings=args['servings'],
            description=args.get('description')
        )
        db.session.add(new_recipe)
        db.session.commit()
        return new_recipe, 201
