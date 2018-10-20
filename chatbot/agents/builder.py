from chatbot.agents.forecast import ForecastAgent
from chatbot.agents.exceptions import UndefinedAgent

FORECAST_AGENT = 'CheckWeather'

AGENT_BY_NAME = {
    FORECAST_AGENT: ForecastAgent,
}


def build_agent_by_intent_diplayname(name):
    """Get a tax declaration manager class depending on the given currency and instantiate the object."""
    agent = AGENT_BY_NAME.get(name, None)
    if agent:
        return agent()
    else:
        raise UndefinedAgent(name)


def get_intent_display_name(post):
    intent_display_name = None
    try:
        intent_display_name = post.get('queryResult').get('intent').get('displayName')
    except AttributeError:
        intent_display_name = None

    try:
        intent_display_name = intent_display_name or post.get('result').get('action')
    except AttributeError:
        intent_display_name = None

    return intent_display_name
