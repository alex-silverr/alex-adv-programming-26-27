import logging
from flask import request, redirect, jsonify, current_app
from flask_restful import Resource
from sqlalchemy.orm import Session
from src.models import User
from src.connect import (makeUser, getAllUsers, getUser, updateInfoTicket)
from src import dbeng

class ManageUsers(Resource):
    """
    MANAGE API
    MODEL: User List
    """
    def get(self):
        """
        Manage Users:
        READ all
        """
        try:
            return jsonify(
                [user.serialize() for user in getAllUsers()]
            )
        
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
    
    def post(self):
        """
        Manage Users:
        CREATE new
        """
        try:
            newuser = makeUser(request.json)
            if newuser:
                return redirect("/users")
            else:
                raise Exception("User not created.")

        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class ManageUser(Resource):
    """
    MANAGE API
    MODEL: User Instance
    """
    def get(self, id):
        """
        Manage User:
        READ one
        """
        try:
            return jsonify(getUser(id).serialize())
        
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
        
    def patch(self, id):
        """
        Manage User:
        UPDATE one
        """
        try:
            user = updateInfoTicket(id, request.json)
            if user:
                return redirect("/users")
            else:
                raise Exception("User not returned correctly")

        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

    def delete(self, id):
        """
        Manage User:
        DELETE one
        """
        try:
            id = int(id)
            with Session(dbeng) as session:
                user = session.get(
                    User, id
                )
                session.delete(user)
                session.commit()
            return redirect ("/users")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
