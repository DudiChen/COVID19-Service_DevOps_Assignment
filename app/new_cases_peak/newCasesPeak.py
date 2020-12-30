from flask import request, Blueprint, jsonify
from app.data_handler.corona_data_handler import DataHandler

cases_blueprint = Blueprint('cases_blueprint', __name__)


@cases_blueprint.route('/newCasesPeak', methods=['GET'])
def get_new_cases_peak_by_country():
    country = request.args.get('country')
    response = {}
    if type(country) == str:
        data_handler = DataHandler()
        result = data_handler.get_new_cases_peak_data(country)
        if result:
            response = {"country": country, "method": "newCasesPeak"}
            response["date"] = result["date"]
            response["value"] = result["amount"]

    return jsonify(response), 200


