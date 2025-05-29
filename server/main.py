from flask import Flask, abort, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import pprint


app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
CORS(app, resources={r"/*": {"origins": ["http://localhost:5500", "http://127.0.0.1:5500"]}})
db = SQLAlchemy(app)

class FarmModel(db.Model):
    __tablename__ = 'farms'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    location = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100))
    image = db.Column(db.String(100), nullable = False)

class CoffeeModel(db.Model):
    __tablename__ = 'coffees'
    id = db.Column(db.Integer, primary_key = True)
    farm_id = db.Column(db.Integer, nullable = False)
    variety = db.Column(db.String(100), nullable = False)
    process = db.Column(db.String(100), nullable = False)
    descriptors = db.Column(db.String(100), nullable = False)
    image = db.Column(db.String(100), nullable = False)
    url_name = db.Column(db.String(100), nullable = False, unique = True)

coffee_resource_fields = {
      'id': fields.Integer,
      'farm_id': fields.Integer,
      'variety': fields.String,
      'process': fields.String,
      'descriptors': fields.String,
      'image': fields.String,
      'url_name': fields.String
}

farm_resource_fields = {
      'id': fields.Integer,
      'name': fields.String,
      'location': fields.String,
      'description': fields.String,
      'image': fields.String
}

class ApiFarmCollection(Resource):

    @marshal_with(farm_resource_fields)
    def get(self):
        result = FarmModel.query.all()
        return result, 200
    
    @marshal_with(farm_resource_fields)
    def post(self):
        args = farm_parse_args.parse_args()

        if db.session.query(FarmModel).filter_by(name = args['name']).count() > 0:
            return () , 409

        farm = FarmModel(id = len(FarmModel.query.all())+1, location = args['location'],
                         name = args['name'], description = args['description'], image = args['image'])
        
        db.session.add(farm)
        db.session.commit()

        return farm, 201

    
class ApiCoffeeCollection(Resource):

    @marshal_with(coffee_resource_fields)
    def get(self):
        result = CoffeeModel.query.all()
        return result, 200
    
    def generate_url_name(self, farm_name, variety, process):
        farm_name = farm_name.lower()
        farm_name = farm_name.replace(" ", "_")

        variety = variety.lower()
        variety = variety.replace(" ", "_")

        process = process.lower()
        process = process.replace(" ", "_")

        url_name = f"{farm_name}/{variety}/{process}"

        return url_name
    
    @marshal_with(coffee_resource_fields)
    def post(self):
        args = coffee_parse_args.parse_args()

        if db.session.query(FarmModel).filter_by(id = args['farm_id']).count() == 0:
            return "please provide valid farm id", 400
        
        farm_name = FarmModel.query.get(args['farm_id']).name
        
        args['url_name'] = self.generate_url_name(farm_name, args['variety'], args['process'])

        coffee = CoffeeModel(id = len(CoffeeModel.query.all())+1, farm_id = args['farm_id'], variety = args['variety'],
                         process = args['process'], descriptors = args['descriptors'], image = args['image'], 
                         url_name = args['url_name'])
        
        db.session.add(coffee)
        db.session.commit()

        return coffee, 201

class ApiFarmIndex(Resource):
    
    @marshal_with(farm_resource_fields)
    def get(self, index):
        result = FarmModel.query.get(index)
        return result, 200
    
    #@marshal_with(farm_resource_fields)
    def delete(self, index):
        farm = FarmModel.query.get(index)
        db.session.delete(farm)
        db.session.commit()
        return (), 200

    
class ApiCoffeeIndex(Resource):
    
    @marshal_with(coffee_resource_fields)
    def get(self, index):
        result = CoffeeModel.query.get(index)
        return result, 200

with app.app_context():
    db.create_all()

api.add_resource(ApiFarmCollection,"/api/farms")
api.add_resource(ApiFarmIndex,"/api/farms/<int:index>") 

api.add_resource(ApiCoffeeCollection,"/api/coffees")
api.add_resource(ApiCoffeeIndex,"/api/coffees/<int:index>") 


farm_parse_args = reqparse.RequestParser() # заменили form на json чтобы отправлять из JS
farm_parse_args.add_argument('name', type=str, help='provide the name of this farm', required=True, location='json')
farm_parse_args.add_argument('location', type=str, help='provide the country name of this farm', required=True, location='json')
farm_parse_args.add_argument('description', type=str, help='provide the country name of this farm',location='json')
farm_parse_args.add_argument('image', type=str, help='url adress of a photo',location='json')


coffee_parse_args = reqparse.RequestParser()
coffee_parse_args.add_argument('farm_id', type=int, help='shows connection of a coffee with a farm', required=True,location='form')
coffee_parse_args.add_argument('variety', type=str, help='provide the variety of a coffee', required=True,location='form')
coffee_parse_args.add_argument('process', type=str, help='provide the processing method',location='form')
coffee_parse_args.add_argument('descriptors', type=str, help='gives taste descriptors of a coffee',location='form')
coffee_parse_args.add_argument('image', type=str, help='url adress of a photo',location='form')
coffee_parse_args.add_argument('url_name', type=str, help='url of a coffee ',location='form')
     
if __name__ == "__main__":
    app.run(debug = True)