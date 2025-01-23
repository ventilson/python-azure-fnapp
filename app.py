import os
from flask import Flask, request, jsonify
import logging
from dotenv import load_dotenv

from function1.function1_logic import handle_request as function1_request_handler
from function2.function2_logic import handle_request as function2_request_handler

load_dotenv()

app = Flask(__name__)

# logging.basicConfig(level=logging.DEBUG) # Set the logging level

@app.route("/api/function1", methods=["GET"])
def function1():
     return function1_request_handler(request)


@app.route("/api/function2", methods=["POST"])
def function2():
    return function2_request_handler(request)

if __name__ == '__main__':
     logging.info("Starting the application...")
     app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))