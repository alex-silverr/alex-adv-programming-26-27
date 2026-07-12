from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify)
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

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