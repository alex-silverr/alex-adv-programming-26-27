import logging
from flask import (request, redirect, jsonify, current_app)
from flask_restful import Resource
from src.connect import searchTicket, getTicket


class ReadTicketList(Resource):
    """
    Ticket READ:
    Search list of Tickets
    """
    def get(self):
        try:
            return jsonify(searchTicket(request.args))
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
        
class ReadTicketInstance(Resource):
    """
    Ticket READ:
    Get Ticket instance
    """
    def get(self, id):
        try:
            return jsonify(getTicket(id))
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
