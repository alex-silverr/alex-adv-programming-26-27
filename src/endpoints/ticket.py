import logging
from flask import (request, redirect, jsonify, current_app)
from flask_restful import Resource
from src.connect import (makeTicket, searchTicket, getTicket,
                         updateInfoTicket, addHistoryTicket,
                         assignToUserTicket, updateEstimatedTimeTicket,
                         changeStatusTicket)


class CreateTicket(Resource):
    """
    Ticket CREATE:
    Create new ticket
    """
    def post(self):
        try:
            newticket = makeTicket(request.json)
            if newticket:
                return redirect("/tickets")
            else:
                raise Exception("Ticket not created.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class ReadTicketList(Resource):
    """
    Ticket READ:
    Search list of Tickets
    """
    def get(self):
        try:
            return jsonify(
                [ticket.serialize() for ticket in searchTicket(request.args)]
            )
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
            return jsonify(getTicket(id).serialize())
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
        
class UpdateTicketUpdateInfo(Resource):
    """
    Ticket UPDATE:
    Change general Ticket information
    """
    def post(self, id):
        try:
            ticket = updateInfoTicket(id, request.json)
            if ticket:
                return redirect("/tickets")
            else:
                raise Exception("Ticket not returned correctly.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class UpdateTicketAddHistoryEvent(Resource):
    """
    Ticket UPDATE:
    Add Event to Ticket history
    """
    def post(self, id):
        try:
            ticket = addHistoryTicket(id, request.json)
            if ticket:
                return redirect("/tickets")
            else:
                raise Exception("Ticket not returned correctly.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class UpdateTicketAssignUser(Resource):
    """
    Ticket UPDATE:
    Assign User to Ticket
    """
    def post(self, id):
        try:
            ticket = assignToUserTicket(id, request.json)
            if ticket:
                return redirect("/tickets")
            else:
                raise Exception("Ticket not returned correctly.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class UpdateTicketEstimatedTime(Resource):
    """
    Ticket UPDATE:
    Change Ticket estimated time
    """
    def post(self, id):
        try:
            ticket = updateEstimatedTimeTicket(id, request.json)
            if ticket:
                return redirect("/tickets")
            else:
                raise Exception("Ticket not returned correctly.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class UpdateTicketChangeStatus(Resource):
    """
    Ticket UPDATE:
    Chang Ticket status
    """
    def post(self, id):
        try:
            ticket = changeStatusTicket(id, request.json)
            if ticket:
                return redirect("/tickets")
            else:
                raise Exception("Ticket not returned correctly.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
