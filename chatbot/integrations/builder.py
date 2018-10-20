from chatbot.integrations.openweathermap import OpenWeatherMapIntegration
from chatbot.integrations.exceptions import UndefinedIntegration

OPEN_WEATHER_MAP = 'openweathermap'

INTEGRATIONS_BY_NAME = {
    OPEN_WEATHER_MAP: OpenWeatherMapIntegration,
}


def build_integration_by_source(name):
    """Get a tax declaration manager class depending on the given currency and instantiate the object."""
    integration = INTEGRATIONS_BY_NAME.get(name, None)
    if integration:
        return integration()
    else:
        raise UndefinedIntegration(name)
