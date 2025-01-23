import logging
import azure.functions as func
import json
from langchain_community.tools.tavily_search import TavilySearchResults
        

def handle_request(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP POST trigger function processed a request in function2 logic.')

    try:
         req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Please provide a JSON body with 'question' for function2 (POST).",
            status_code=400
        )

    question = req_body.get('question')

    if question:
        tavily_search = TavilySearchResults(max_results=3)
        search_docs = tavily_search.invoke(question)

        return func.HttpResponse(
            json.dumps(search_docs),
            status_code=200
        )
    else:
        return func.HttpResponse(
            "Please provide 'question' in the JSON body for function2 (POST).",
            status_code=400
        )