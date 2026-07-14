from flask import render_template, make_response
from flask_restful import Resource

class Index(Resource):
    """
    Default/placeholder index
    """
    def get(self):
        return make_response(render_template("home.html"))
    

class ErrorLanding(Resource):
    """
    Default/placeholder error page
    """
    def get(self):
        return make_response(render_template("error_placeholder.html"))