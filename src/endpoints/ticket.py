import logging
from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify, current_app)
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select, desc
from sqlalchemy.orm import Session
from ..database import Base, Thing, dbeng
from ..models.ticket import Ticket
from ..models.event import Event
from ..models.user import User
from ..connect.ticket import searchTicket, getTicket
from ..models.options import (PriorityLevel, TicketType, 
                              EditedField, TicketStatus, 
                              UserRole, EventType)
from ..settings import SQLALCHEMY_DATABASE_URL


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
