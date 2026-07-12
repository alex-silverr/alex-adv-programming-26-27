import logging
from flask import (request, redirect, jsonify, current_app)
from flask_restful import Resource
# from src.connect import () TODO

class CreateUser(Resource):
    # TODO
    def post(self):
        pass

class ReadUserList(Resource):
    # TODO
    def get(self):
        pass

class ReadUserInstance(Resource):
    # TODO
    def get(self, id):
        pass

class UpdateUserInfo(Resource):
    # TODO
    def post(self, id):
        pass

class DeleteUser(Resource):
    # TODO
    def post(self, id):
        pass