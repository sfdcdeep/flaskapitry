import importlib
import os
from flask import Flask, request
from flask_restful import Resource, Api

sendres = {"result": "Success"}

#Dyno started
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
	def get(self):
		return {"about":"hellow world"}
	def post(self):
                some_json = request.get_json()
                return {"you sent" : some_json}, 201

class Multi(Resource):
        
        def get(self, fyl):
                PLUGIN_NAME = fyl
                #return(PLUGIN_NAME)
                plugin_module=importlib.import_module(PLUGIN_NAME, ".")
                """
                if not plugin_module:
                        return('Failed')
                else:
                        return('Python File Executed Successfully')
                """
        def post(self):
                #args = parser.parse_args()
                #return sendres, 201
                print('Python file is executed')

#api.add_resource(HelloWorld, '/')
api.add_resource(Multi, '/multi/<string:fyl>')


                                       

"""
if __name__ == '__main__':
	app.run(debug=True)

"""
