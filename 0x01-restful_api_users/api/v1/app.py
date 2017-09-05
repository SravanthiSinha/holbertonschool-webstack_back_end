from flask import Flask
from flask import jsonify
from os import getenv
from api.v1.views import app_views

env_port = getenv('HBNB_API_PORT')
env_host = getenv('HBNB_API_HOST')

app = Flask(__name__)
app.register_blueprint(app_views)

if __name__ == '__main__':
    if(env_port is not None and env_host is not None):
        app.run(host=env_host, port=int(env_port))
    else:
        app.run()
