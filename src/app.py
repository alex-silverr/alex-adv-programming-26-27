from flask import Flask, render_template, make_response, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

things = ["thing 1", "thing 2", "thing 3"]

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
    def get(self):
        index = request.args.get('thing')
        app.logger.debug(index)
        if index:
            return things[index]
        return things


api.add_resource(Index, "/")
api.add_resource(ShowThings, "/things")

if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080', debug=True)