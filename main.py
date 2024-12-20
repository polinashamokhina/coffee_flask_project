from flask import Flask, abort, request
from flask_restful import Api, Resource, reqparse, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy 
import json

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class FarmModel(db.Model):
    __tablename__ = 'farms'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False, unique = True)
    location = db.Column(db.String(100), nullable = False)
    description = db.Column(db.String(100))

farm_resource_fields = {
      'id': fields.Integer,
      'name': fields.String,
      'location': fields.String,
      'description': fields.String
}

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

# with app.app_context():
#     db.create_all()

api.add_resource(ApiFarmCollection,"/api/farm")

farm_parse_args = reqparse.RequestParser()
farm_parse_args.add_argument('name', type=str, help='provide the name of this farm', required=True)
farm_parse_args.add_argument('location', type=str, help='provide the country name of this farm', required=True)
farm_parse_args.add_argument('description', type=str, help='provide the country name of this farm')
     
if __name__ == "__main__":
    app.run(debug = True)