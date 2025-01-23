import logging
import azure.functions as func
import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

def handle_request(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP GET trigger function processed a request in function1 logic.')

    item_name = req.params.get('item_name')

    if item_name:
        llm = ChatOpenAI(model="gpt-4o", temperature=0) 

        messages = [HumanMessage(content=f"I want to learn more about {item_name}.", name="Lance")]
        result = llm.invoke(messages)

        response_message = {
            "metadata": result.response_metadata,
            "response": result.content
        }

        return func.HttpResponse(
            json.dumps(response_message),
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Please provide 'name' and 'age' in the query string for function1 (GET).",
            status_code=400
        )