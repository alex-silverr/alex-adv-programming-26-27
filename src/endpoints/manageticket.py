import logging
from flask import request, redirect, jsonify, current_app
from flask_restful import Resource
from src.connect import (makeTicket, getAllTickets, getTicket,
                        generalUpdateTicket, hardDeleteTicket)

class ManageTickets(Resource):
    """
    MANAGE API
    MODEL: Ticket List
    """
    def get(self):
        """
        Manage Ticket:
        READ all
        """
        try:
            return jsonify(
                [ticket.serialize() for ticket in getAllTickets()]
            )
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
    
    def post(self):
        """
        Manage Ticket:
        CREATE new
        """
        try:
            newticket = makeTicket(request.json)
            if newticket:
                return redirect("/tickets")
            else:
                raise Exception("Ticket not created.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class ManageTicket(Resource):
    """
    MANAGE API
    MODEL: Ticket Instance
    """
    def get(self, id):
        """
        Manage Ticket:
        READ one
        """
        try:
            return jsonify(getTicket(id).serialize())    
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
        
    def patch(self, id):
        """
        Manage Ticket:
        UPDATE one
        """
        try:
            ticket = generalUpdateTicket(id, request.json)
            if ticket:
                return redirect("/tickets")
            else:
                raise Exception("Ticket not returned correctly.")

        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

    def delete(self, id):
        """
        Manage Ticket:
        DELETE one
        """
        try:
            if hardDeleteTicket(id):
                return redirect ("/things")
            else:
                raise Exception("Ticket not deleted correctly.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
