import logging
import os
import json
from flask import jsonify
from langchain_community.tools.tavily_search import TavilySearchResults
        

def handle_request(req) -> jsonify:
    logging.info('Python HTTP POST trigger function processed a request in function2 logic.')

    try:
         req_body = req.get_json()
    except ValueError:
        return jsonify(
            message="Please provide a JSON body with 'question' for function2 (POST)."
            ), 400

    question = req_body.get('question')

    if question:
        tavily_search = TavilySearchResults(max_results=3)
        search_docs = tavily_search.invoke(question)

        return jsonify(
            search_docs
        ), 200
    else:
        return jsonify(
            message="Please provide 'question' in the JSON body for function2 (POST)."
        ), 400