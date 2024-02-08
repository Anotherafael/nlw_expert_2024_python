from src.views.http_types.http_response import HttpResponse

from .error_types.http_unprocessable_entity import HttpUnprocessabelEntityError


def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessabelEntityError):
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [
                    {
                        "title": "Unprocessable Entity",
                        "description": error.message,
                    }
                ],
            },
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors": [
                {
                    "title": "Server Error",
                    "description": str(error),
                }
            ],
        },
    )
