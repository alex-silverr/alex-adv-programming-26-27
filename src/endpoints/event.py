import logging
from flask import (request, redirect, jsonify, current_app)
from flask_restful import Resource
from src.connect import (searchEvent ,getEvent, makeEvent)

class CreateEvent(Resource):
    """
    Event CREATE:
    Create new Event
    """
    def post(self):
        try:
            newevent = makeEvent(request.json)
            if newevent:
                return redirect("/event")
            else:
                raise Exception("Event not created.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
        
class CreateHistoryEvent(Resource):
    """
    Event CREATE:
    Create new Event
    """
    def post(self):
        try:
            newevent = makeEvent(
                request.json | { 
                    "event_type": "History Entry Added"
                }
            )
            if newevent:
                return redirect("/event")
            else:
                raise Exception("Event not created.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class ReadEventList(Resource):
    """
    Event READ:
    Search list of Events
    """
    def get(self):
        try:
            return jsonify(
                [event.serialize() for event in searchEvent(request.args)]
            )
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class ReadEventInstance(Resource):
    """
    Event READ:
    Get Event instance
    """
    def get(self, id):
        try:
            return jsonify(getEvent(id).serialize())
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")