from flask import Flask, request, jsonify
from app.new_cases_peak.newCasesPeak import cases_blueprint
from app.recovered_peak.recoveredPeak import recovered_blueprint
from app.deaths_peak.deathsPeak import deaths_blueprint
from app.status.status import status_blueprint


app = Flask(__name__)
app.register_blueprint(cases_blueprint)
app.register_blueprint(recovered_blueprint)
app.register_blueprint(deaths_blueprint)
app.register_blueprint(status_blueprint)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
