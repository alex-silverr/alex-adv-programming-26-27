import logging
from flask import (request, redirect, jsonify, current_app)
from flask_restful import Resource
from src.connect import (makeTicket, searchTicket, getTicket,
                         updateInfoTicket, addHistoryTicket,
                         assignToUserTicket, updateEstimatedTimeTicket,
                         changeStatusTicket)

# CREATE: Create new - OK
# READ: Read all - OK
# READ: Search by filter - OK
# READ: Get by ID - OK
# UPDATE: Edit info (Title, Description, Priority) - TODO
# UPDATE: Add history item - TODO
# UPDATE: Assign to user - TODO
# UPDATE: Change estimated time - TODO
# UPDATE: Change status ("DELETE": Removed status) - TODO

class MakeTicket(Resource):
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
    def patch(self, id):
        pass

class UpdateTicketAddHistoryEvent(Resource):
    """
    Ticket UPDATE:
    Add Event to Ticket history
    """
    def post(self, id):
        pass

class UpdateTicketAssignUser(Resource):
    """
    Ticket UPDATE:
    Assign User to Ticket
    """
    def post(self, id):
        pass

class UpdateTicketEstimatedTime(Resource):
    """
    Ticket UPDATE:
    Change Ticket estimated time
    """
    def patch(self, id):
        pass

class UpdateTicketChangeStatus(Resource):
    """
    Ticket UPDATE:
    Chang Ticket status
    """
    def patch(self, id):
        pass
