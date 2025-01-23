import logging
import os
import json
from flask import jsonify
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

def handle_request(req) -> jsonify:
    logging.info('Python HTTP GET trigger function processed a request in function1 logic.')

    item_name = req.args.get('item_name')

    if item_name:
        llm = ChatOpenAI(model="gpt-4o", temperature=0) 

        messages = [HumanMessage(content=f"I want to learn more about {item_name}.", name="Lance")]
        result = llm.invoke(messages)

        response_message = {
            "metadata": result.response_metadata,
            "response": result.content
        }

        return jsonify(
            response_message
        ), 200
    else:
        return jsonify(
            message="Please provide 'name' and 'age' in the query string for function1 (GET).",
        ), 400