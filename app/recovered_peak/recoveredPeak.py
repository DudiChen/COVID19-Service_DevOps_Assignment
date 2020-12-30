from flask import request, Blueprint, jsonify
from app.data_handler.corona_data_handler import DataHandler

recovered_blueprint = Blueprint('recovered_blueprint', __name__)


@recovered_blueprint.route('/recoveredPeak', methods=['GET'])
def get_recovered_peak_by_country():
    country = request.args.get('country')
    response = {}
    if type(country) == str:
        data_handler = DataHandler()
        result = data_handler.get_recovered_peak_data(country)
        if result:
            response = {"country": country, "method": "recoveredPeak"}
            response["date"] = result["date"]
            response["value"] = result["amount"]

    return jsonify(response), 200
