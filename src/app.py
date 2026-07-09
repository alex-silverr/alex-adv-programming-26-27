from flask import Flask, render_template, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

Things = []

class Index(Resource):
    """
    Default/placeholder index
    """
    def get(self):
        return make_response(render_template("home.html"))

class ShowThings(Resource):
    """
    Barebones API: page that shows "things" list
    """
    def get(self, index=None):
        return Things[index] if index else Things


api.add_resource(Index, "/")
api.add_resource(ShowThings, "/things/<int:num>")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')