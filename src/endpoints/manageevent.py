import logging
from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify, current_app)
from flask_restful import Resource
from sqlalchemy import select
from sqlalchemy.orm import Session
from src import dbeng
# from src.models import Ticket, Event, User, EventType
from src.connect import (getEvent, getAllEvents, makeEvent, 
                         hardDeleteEvent, updateInfoEvent)

class ManageEvents(Resource):
    """
    MANAGE API
    MODEL: Event List
    """
    def get(self):
        """
        Manage Events:
        READ all
        """
        try:
            return jsonify(
                [event.serialize() for event in getAllEvents()]
            )
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
    
    def post(self):
        """
        Manage Events:
        CREATE new
        """
        try:
            newevent = makeEvent(request.json)
            if newevent:
                return redirect("/events")
            else:
                raise Exception("Event not created.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class ManageEvent(Resource):
    """
    MANAGE API
    MODEL: Event Instance
    """
    def get(self, id):
        """
        Manage Event:
        READ one
        """
        try:
            return jsonify(getEvent(id).serialize())
        
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
        
    def patch(self, id):
        """
        Manage Event:
        UPDATE one
        """
        try:
            event = updateInfoEvent(id, request.json)
            if event:
                return redirect("/events")
            else:
                raise Exception("Event not returned correctly.")

        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

    def delete(self, id):
        """
        Manage Event:
        DELETE one
        """
        try:
            if hardDeleteEvent(id):
                return redirect ("/events")
            else:
                raise Exception("Event not deleted correctly.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
