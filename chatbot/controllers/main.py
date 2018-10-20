import json

from chatbot.agents.builder import (
    build_agent_by_intent_diplayname,
    get_intent_display_name,
)
from chatbot.settings import app
from flask import request
from flask import make_response
from chatbot.routes import APP_ROUTES
from chatbot.views.main import IndexView


# routes
webhook_route = APP_ROUTES.get('webhooks')
index_route = APP_ROUTES.get('index')


class Controller(object):

    @app.route(webhook_route.get('route'), methods=webhook_route.get('methods'))
    def webhook():
        post = request.get_json(silent=True, force=True)
        print(post)
        intent_display_name = get_intent_display_name(post)
        agent = build_agent_by_intent_diplayname(intent_display_name)
        agent.request_url = request.url
        return_value = agent.process_request(post)
        return_value = json.dumps(return_value, indent=4)
        # Convert the return value from a view function to an instance of response_class.
        response = make_response(return_value)
        response.headers['Content-Type'] = 'application/json'
        return response

    @app.route(index_route.get('route'))
    def index():
        iframe = IndexView()
        return iframe.render()
