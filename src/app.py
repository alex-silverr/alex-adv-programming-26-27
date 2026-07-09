from flask import Flask, render_template, make_response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Index(Resource):
    """
    Default/placeholder index
    """
    def get(self):
        return make_response(render_template("home.html"))

api.add_resource(Index, "/")
# @app.route("/")
# def home():
#     """
#     This is a default/placeholder page to test if I understood how Flask works.
#     """
#     return render_template("home.html")

# This is from the Flask tutorial given in class
if __name__ == "__main__":
    app.run(host='0.0.0.0',port='8080')