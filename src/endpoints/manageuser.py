import logging
from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify, current_app)
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from src.models import User, UserRole
from src.connect import (makeUser, getAllUsers, getUser)
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
            id = int(id)
            data = request.json
            with Session(dbeng) as session:
                user = session.get(
                    User, id
                )
                if "display_name" in data: user.display_name = data.get("display_name")
                if "full_name" in data: user.full_name = data.get("full_name")
                if "email" in data: user.email = data.get("email")
                if "github" in data: user.github = data.get("github")
                if "role_id" in data: user.r_role = session.get(
                    UserRole, data.get("role_id")
                )
                session.commit()
            return redirect("/users")

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
