from flask import Flask, abort, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy 
import json

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

def to_json(object):
    return json.dumps(object, default=lambda o: o.__dict__)

class FarmModel(db.Model):
    __tablename__ = 'farms'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    location = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100))

class CoffeeModel(db.Model):
    __tablename__ = 'coffees'
    id = db.Column(db.Integer, primary_key = True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farms.id'))
    variety = db.Column(db.String(100), nullable = False)
    process = db.Column(db.String(100), nullable = False)
    descriptors = db.Column(db.String(100), nullable = False)
    image = db.Column(db.String(300), nullable = False)
    url_name = db.Column(db.String(300), nullable = False)

farm_resource_fields = {
      'id': fields.Integer,
      'name': fields.String,
      'location': fields.String,
      'description': fields.String
}

coffee_resource_fields = {
      'id': fields.Integer,
      'farm_id': fields.Integer,
      'variety': fields.String,
      'process': fields.String,
      'descriptors': fields.String,
      'image': fields.String,
      'url_name': fields.String
}

# with app.app_context():
#     db.create_all()

class Farm:

    def __init__(self, id, location, name, description):
        self.id = id 
        self.location = location
        self.name = name
        self.description = description 

farm_arr = []

class Coffee:
    def __init__(self, id, farm_name, variety, process, descriptors, image, url_name):
        self.id = id
        self.farm_name = farm_name
        self.variety = variety
        self.process = process
        self.descriptors = descriptors
        self.image = image
        self.url_name = url_name
    
coffee_arr = []

class ApiFarmCollection(Resource):

    @marshal_with(farm_resource_fields)
    def get(self):
        result = FarmModel.query.all()
        return result
    
    @marshal_with(farm_resource_fields)
    def post(self):
        args = farm_parse_args.parse_args()

        farm = FarmModel(id = len(FarmModel.query.all())+1, location = args['location'],
                         name = args['name'], description = args['description'])
        
        db.session.add(farm)
        db.session.commit()

        return farm, 201
    
class ApiCoffeeCollection(Resource):
    def get(self):
        return {"data": to_json(coffee_arr)} 

    def generate_url_name(self, farm_name, variety, process):
        farm_name = farm_name.lower()
        farm_name = farm_name.replace(" ", "_")

        variety = variety.lower()
        variety = variety.replace(" ", "_")

        process = process.lower()
        process = process.replace(" ", "_")

        url_name = f"{farm_name}/{variety}/{process}"

        return url_name

    def post(self):
        args = coffee_parse_args.parse_args()

        id = len(coffee_arr) + 1
        #farm_id = request.form["farm_id"] #должны знать айди фермы, обычный пользователь не может, это странно
        farm_name = request.form["farm_name"] 
        variety = request.form["variety"] #request  - запрос - форма = данные от пользователя
        process = request.form["process"]  
        descriptors = request.form["descriptors"] # надо удобно читать код 
        image = request.form["image"]

        farm_name_verification = next((f for f in farm_arr if f.name == farm_name), None)
        if not farm_name_verification:
            return {"message": f"No farm such as {farm_name} found"}, 400
        
        url_name = self.generate_url_name(farm_name, variety, process)
        
        new_coffee = Coffee(id, farm_name, variety, process, descriptors, image, url_name)
        print(new_coffee)
        coffee_arr.append(new_coffee)
        return new_coffee, 201
    
if __name__ == "__main__":
    app.run(debug = True)