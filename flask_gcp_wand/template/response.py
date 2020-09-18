from flask import current_app, make_response, jsonify
from http import HTTPStatus
from ..appengine.env import GaeEnv
from werkzeug.exceptions import HTTPException


def unexpected_error_response(e: Exception):
    current_app.logger.critical(
        f"Unexpected {e.__class__.__name__}: {e}", exc_info=True
    )
    res = {
        "status": HTTPStatus.INTERNAL_SERVER_ERROR,
        "error": "InternalServerError",
        "errorMessage": "Sorry, unexpected error occurred.",
    }
    if not GaeEnv.is_gae():
        res["errorDetail"] = {
            "exception": e.__class__.__name__,
            "message": str(e),
        }
    return make_response(jsonify(res), HTTPStatus.INTERNAL_SERVER_ERROR)


def not_found_response(e: HTTPException):
    res = {
        "status": HTTPStatus.NOT_FOUND,
        "error": "NotFound",
    }
    return make_response(jsonify(res), HTTPStatus.NOT_FOUND)
