import logging
from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify, current_app)
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from src.connect import makeTicket, getAllTickets, getTicket
from src import dbeng, SQLALCHEMY_DATABASE_URL
from src.models import (Ticket, Event, User, TicketType,
                        TicketStatus, PriorityLevel)

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
            return jsonify(getAllTickets())
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
            return jsonify(getTicket(id))    
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
        
    def patch(self, id):
        """
        Manage Ticket:
        UPDATE one
        """
        try:
            id = int(id)
            data = request.json
            with Session(dbeng) as session:
                ticket = session.get(
                    Ticket, id
                )
                if "title" in data: ticket.title = data.get("title")
                if "description" in data: ticket.description = data.get("description")
                if "estimated_time" in data: ticket.estimated_time = data.get("estimated_time")
                if "priority_id" in data:
                    ticket.r_priority = session.get(
                        PriorityLevel, data.get("priority_id")
                    )
                if "ticket_type_id" in data:
                    ticket.r_ticket_type = session.get(
                        TicketType, data.get("ticket_type_id")
                    )
                if "status_id" in data:
                    ticket.r_status = session.get(
                        TicketStatus, data.get("status_id")
                    )
                session.commit()
            return redirect("/tickets")

        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

    def delete(self, id):
        """
        Manage Ticket:
        DELETE one
        """
        try:
            id = int(id)
            with Session(dbeng) as session:
                ticket = session.get(
                    Ticket, id
                )
                session.delete(ticket)
                session.commit()
            return redirect ("/things")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
