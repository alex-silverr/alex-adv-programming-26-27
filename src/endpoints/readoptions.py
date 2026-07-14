import logging
from flask import request, redirect, jsonify, current_app
from flask_restful import Resource
from src.connect import (optionGetAll, optionGetById,
                        optionDelete, optionCreateIfNotExist)

class OptionReadList(Resource):
    """
    LIST OPTIONS API
    """
    def get(self, table):
        try:
            return jsonify(
                [option.serialize() for option in optionGetAll(table)]
            )
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
        
    def post(self, table):
        try:
            if optionCreateIfNotExist(
                    table, request.json.get("desc")
                    ):
                return redirect(f"/options/{table}")
            else:
                raise Exception("Something bad happened.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")
        
class OptionsReadInstance(Resource):
    """
    INSTANCE OPTIONS API
    """
    def get(self, table, id):
        try:
            return jsonify(
                optionGetById(table, id).serialize()
            )
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")

    def delete(self, table, id):
        try:
            if optionDelete(table, id):
                return redirect (f"/options/{table}")
            else:
                raise Exception("Something bad happened.")
        except Exception as e:
            current_app.logger.error(e)
            return redirect("/oops")