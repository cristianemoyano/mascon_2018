from chatbot.settings import (
    DEBUG,
    PORT,
    app
)
from chatbot.controllers.main import Controller


if __name__ == '__main__':
    Controller()
    print("Starting app on port %d" % PORT)
    app.run(debug=DEBUG, port=PORT, host='0.0.0.0')
