from flask import Blueprint, jsonify, request

from src.errors.error_handler import handle_errors
from src.views.http_types.http_request import HttpRequest
from src.views.tag_creator_view import TagCreatorView

tag_routes_bp = Blueprint("tag_routes", __name__)


@tag_routes_bp.route("/create_tag", methods=["POST"])
def create_tag():
    response = None
    try:
        tag_creator_view = TagCreatorView()
        http_request = HttpRequest(
            header=request.headers,
            body=request.json,
            query_params=request.args,
        )
        response = tag_creator_view.validate_and_create(http_request)
    except Exception as error:
        response = handle_errors(error)

    return (
        jsonify(
            {
                "body": response.body,
                "status_code": response.status_code,
            }
        ),
        response.status_code,
    )
