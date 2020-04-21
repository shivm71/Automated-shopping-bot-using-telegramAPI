import logging.config
from flask import Flask, request, Response, jsonify

log = logging.getLogger(__name__)
app = Flask(__name__)

@app.route('/isActive')
def is_active():
    return 'ACTIVE'

@app.route('/')
def is_server_up():
    return 'Server is running'

if __name__ == "__main__":
    """
    Main method used for local development only
    """
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<')
    app.run(host='localhost', debug=True, port=8000)