import logging
from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify, current_app)
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from src import Thing, dbeng

# -------------------------
#  Thing and Things
# -------------------------
    
class ManageThings(Resource):
    """
    Barebones API: list resource
    """

    def get(self):
        """
        Barebones API: list READ
        Returns all things
        """
        with Session(dbeng) as session:
            things = session.scalars(
                select(Thing)
                .order_by(Thing.id)
            ).all()
        return jsonify([t.serialize() for t in things])
    
    def post(self):
        """
        Barebones API: CREATE
        Creates new thing
        """
        thing = request.json.get("thing")
        if thing:
            with Session(dbeng) as session:
                newthing = Thing(thing=thing)
                session.add(newthing)
                session.commit()
        else:
            current_app.logger.error("No thing to add")
            return redirect("/oops")
        return redirect("/things")
    
class ManageThing(Resource):
    """
    Barebones API: instance resource
    """

    def get(self, index=None):
        """
        Barebones API: instance READ
        Returns a thing
        """
        try:
            index = int(index)
            with Session(dbeng) as session:
                thing = session.get(
                    Thing, index
                )
            return jsonify(thing.serialize())
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

    def put(self, index=None):
        """
        Barebones API: UPDATE
        Changes content of a thing
        """
        try:
            index = int(index)
            thingv = request.json.get("thing")
            if not thingv:
                current_app.logger.error("No update value for instance given")
                return redirect("/oops")
            else:
                with Session(dbeng) as session:
                    thing = session.get(
                        Thing, index
                    )
                    thing.thing = thingv
                    session.commit()
                return redirect("/things")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
        
    def delete(self, index=None):
        """
        Barebones API: DELETE
        Removes a thing
        """
        try:
            index = int(index)
            with Session(dbeng) as session:
                thing = session.get(
                    Thing, index
                )
                session.delete(thing)
                session.commit()
            return redirect("/things")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
