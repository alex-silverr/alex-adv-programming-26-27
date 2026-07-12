import logging
from flask import (Flask, render_template, make_response, 
                   request, redirect, jsonify, current_app)
from flask_restful import Resource
from sqlalchemy import select
from sqlalchemy.orm import Session
from src import dbeng
from src.models import Ticket, Event, User, EventType

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
            with Session(dbeng) as session:
                events = session.scalars(
                    select(Event)
                    .order_by(Event.id)
                ).all()
            return jsonify([event.serialize() for event in events])
        
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
    
    def post(self):
        """
        Manage Events:
        CREATE new
        """
        try:
            data = request.json

            with Session(dbeng) as session:
                newevent = Event(
                    created_by = session.get(
                        User, data.get("user_id")
                    ),
                    ticket = session.get(
                        Ticket, data.get("ticket_id")
                    ),
                    r_event_type = session.get(
                        EventType, data.get("event_type_id")
                    ),
                    description = data.get("description"),
                )
                session.add(newevent)
                session.commit()
            return redirect("/events")

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
            id = int(id)
            with Session(dbeng) as session:
                event = session.get(
                    Event, id
                )
            return jsonify(event.serialize())
        
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
        
    def patch(self, id):
        """
        Manage Event:
        UPDATE one
        """
        try:
            id = int(id)
            data = request.json
            with Session(dbeng) as session:
                event = session.get(
                    Event, id
                )
                if "user_id" in data: event.created_by = session.get(
                    User, data.get("user_id")
                )
                if "ticket_id" in data: event.ticket = session.get(
                    Ticket, data.get("ticket_id")
                )
                if "event_type_id" in data: event.r_event_type = session.get(
                    EventType, data.get("event_type_id")
                )
                if "description" in data: event.description = data.get("description")
                session.commit()
            return redirect("/events")

        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

    def delete(self, id):
        """
        Manage Event:
        DELETE one
        """
        try:
            id = int(id)
            with Session(dbeng) as session:
                event = session.get(
                    Event, id
                )
                session.delete(event)
                session.commit()
            return redirect ("/events")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
