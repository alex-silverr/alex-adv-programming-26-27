import logging
from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify, current_app)
from flask_restful import Resource, Api
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from ..database import Base, Thing, dbeng
from ..models.ticket import Ticket
from ..models.event import Event
from ..models.user import User
from ..models.options import (PriorityLevel, TicketType, 
                              EditedField, TicketStatus, 
                              UserRole, EventType)
from ..settings import SQLALCHEMY_DATABASE_URL

# ------------------------
# Priority Level
# ------------------------
class PriorityReadList(Resource):
    """
    READ API
    MODEL: Priority Level List
    """
    def get(self):
        try:
            with Session(dbeng) as session:
                options = session.scalars(
                    select(PriorityLevel)
                    .order_by(PriorityLevel.id)
                ).all()
            return jsonify([option.serialize() for option in options])
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class PriorityReadInstance(Resource):
    """
    READ API
    MODEL: Priority Level Instance
    """
    def get(self, id):
        try:
            id = int(id)
            with Session(dbeng) as session:
                option = session.get(
                    PriorityLevel, id
                )
            return jsonify(option.serialize())
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

# ------------------------
# Ticket Type
# ------------------------
class TicketTypeReadList(Resource):
    """
    READ API
    MODEL: Ticket Type List
    """
    def get(self):
        try:
            with Session(dbeng) as session:
                options = session.scalars(
                    select(TicketType)
                    .order_by(TicketType.id)
                ).all()
            return jsonify([option.serialize() for option in options])
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class TicketTypeReadInstance(Resource):
    """
    READ API
    MODEL: Ticket Type Instance
    """
    def get(self, id):
        try:
            id = int(id)
            with Session(dbeng) as session:
                option = session.get(
                    TicketType, id
                )
            return jsonify(option.serialize())
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

# ------------------------
# Ticket Status
# ------------------------
class TicketStatusReadList(Resource):
    """
    READ API
    MODEL: Ticket Status List
    """
    def get(self):
        try:
            with Session(dbeng) as session:
                options = session.scalars(
                    select(TicketStatus)
                    .order_by(TicketStatus.id)
                ).all()
            return jsonify([option.serialize() for option in options])
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class TicketStatusReadInstance(Resource):
    """
    READ API
    MODEL: Ticket Status Instance
    """
    def get(self, id):
        try:
            id = int(id)
            with Session(dbeng) as session:
                option = session.get(
                    TicketStatus, id
                )
            return jsonify(option.serialize())
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

# ------------------------
# Event Type
# ------------------------
class EventTypeReadList(Resource):
    """
    READ API
    MODEL: Event Type List
    """
    def get(self):
        try:
            with Session(dbeng) as session:
                options = session.scalars(
                    select(EventType)
                    .order_by(EventType.id)
                ).all()
            return jsonify([option.serialize() for option in options])
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class EventTypeReadInstance(Resource):
    """
    READ API
    MODEL: Event Type Instance
    """
    def get(self, id):
        try:
            id = int(id)
            with Session(dbeng) as session:
                option = session.get(
                    EventType, id
                )
            return jsonify(option.serialize())
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

# ------------------------
# Edited Field
# ------------------------
class EditedFieldReadList(Resource):
    """
    READ API
    MODEL: Edited Fields List
    """
    def get(self):
        try:
            with Session(dbeng) as session:
                options = session.scalars(
                    select(EditedField)
                    .order_by(EditedField.id)
                ).all()
            return jsonify([option.serialize() for option in options])
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class EditedFieldReadInstance(Resource):
    """
    READ API
    MODEL: Edited Fields Instance
    """
    def get(self, id):
        try:
            id = int(id)
            with Session(dbeng) as session:
                option = session.get(
                    EditedField, id
                )
            return jsonify(option.serialize())
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

# ------------------------
# User Role
# ------------------------
class UserRoleReadList(Resource):
    """
    READ API
    MODEL: User Role List
    """
    def get(self):
        try:
            with Session(dbeng) as session:
                options = session.scalars(
                    select(UserRole)
                    .order_by(UserRole.id)
                ).all()
            return jsonify([option.serialize() for option in options])
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

class UserRoleReadInstance(Resource):
    """
    READ API
    MODEL: User Role Instance
    """
    def get(self, id):
        try:
            id = int(id)
            with Session(dbeng) as session:
                option = session.get(
                    UserRole, id
                )
            return jsonify(option.serialize())
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")