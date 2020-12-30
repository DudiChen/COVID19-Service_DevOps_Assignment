from flask import request, Blueprint, jsonify
from app.data_handler.corona_data_handler import DataHandler

status_blueprint = Blueprint('status_blueprint', __name__)


@status_blueprint.route('/status', methods=['GET'])
def get_api_status():
    data_handler = DataHandler()
    response = data_handler.check_api_service_status()
    return jsonify(response), 200
