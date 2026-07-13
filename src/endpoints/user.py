import logging
from flask import (request, redirect, jsonify, current_app)
from flask_restful import Resource
from src.connect import (makeUser, searchUser, getUser, 
                         updateInfoTicket, deleteUser)

class CreateUser(Resource):
    """
    User CREATE:
    Create new User
    """
    def post(self):
        try:
            newuser = makeUser(request.json)
            if newuser:
                return redirect("/users")
            else:
                raise Exception("User not created.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class ReadUserList(Resource):
    """
    User READ:
    Search list of Users
    """
    def get(self):
        try:
            return jsonify(
                [user.serialize() for user in searchUser(request.args)]
            )
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")


class ReadUserInstance(Resource):
    """
    User READ:
    Get User instance
    """
    def get(self, id):
        try:
            return jsonify(getUser(id).serialize())
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class UpdateUserInfo(Resource):
    """
    User UPDATE:
    Change general User information
    """
    def post(self, id):
        try:
            user = updateInfoTicket(id, request.json)
            if user:
                return redirect("/users")
            else:
                raise Exception("User not returned correctly")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class DeleteUser(Resource):
    """
    User DELETE:
    Removes an User
    """
    def post(self, id):
        try:
            if deleteUser(id):
                return redirect("/users")
            else:
                raise Exception("User not deleted correctly.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")