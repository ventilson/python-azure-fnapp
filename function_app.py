import azure.functions as func
import logging

from function1.function1_logic import handle_request as function1_request_handler
from function2.function2_logic import handle_request as function2_request_handler

app = func.FunctionApp()

@app.route(route="function1", auth_level=func.AuthLevel.ANONYMOUS, methods=["GET"])
def function1(req: func.HttpRequest) -> func.HttpResponse:
     return function1_request_handler(req)


@app.route(route="function2", auth_level=func.AuthLevel.ANONYMOUS, methods=["POST"])
def function2(req: func.HttpRequest) -> func.HttpResponse:
    return function2_request_handler(req)