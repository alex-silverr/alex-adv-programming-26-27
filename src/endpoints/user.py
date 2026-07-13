import logging
from flask import (request, redirect, jsonify, current_app)
from flask_restful import Resource
from src.connect import (makeUser, searchUser, getUser)

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
            # TODO
            pass
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
            # TODO
            pass
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")