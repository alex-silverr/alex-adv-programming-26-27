from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify)
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from ..database import Base, Thing
from ..models.ticket import Ticket
from ..models.event import Event
from ..models.user import User
from ..models.options import *
from ..settings import SQLALCHEMY_DATABASE_URL

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