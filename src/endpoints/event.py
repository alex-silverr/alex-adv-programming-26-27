import logging
from flask import (request, redirect, jsonify, current_app)
from flask_restful import Resource
from src.connect import (searchEvent ,getEvent, getAllEvents)

# CREATE: Create new history item
# READ: Read all
# READ: Search by user
# READ: Get by ID

class CreateEvent(Resource):
    """
    Event CREATE:
    Create new Event
    """
    # TODO
    def post(self):
        pass

class ReadEventList(Resource):
    """
    Event READ:
    Search list of Events
    """
    # TODO
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
    # TODO
    def get(self, id):
        try:
            return jsonify(getEvent(id).serialize())
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")