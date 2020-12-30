from flask import request, Blueprint, jsonify
from app.data_handler.corona_data_handler import DataHandler

deaths_blueprint = Blueprint('deaths_blueprint', __name__)


@deaths_blueprint.route('/deathsPeak', methods=['GET'])
def get_deaths_peak_by_country():
    country = request.args.get('country')
    response = {}
    if type(country) == str:
        data_handler = DataHandler()
        result = data_handler.get_deaths_peak_data(country)
        if result:
            response = {"country": country, "method": "deathsPeak"}
            response["date"] = result["date"]
            response["value"] = result["amount"]

    return jsonify(response), 200
