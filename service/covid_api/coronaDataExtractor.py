import requests
from datetime import datetime, timedelta

serverURL = "https://corona.lmao.ninja/v2/"
historicalRequestSuffix = "historical/"


def check_status():
    status_result = {"status": "fail"}
    req_url = serverURL + historicalRequestSuffix
    req_params = {}
    response = requests.get(url=req_url, params=req_params)
    if response.ok:
        status_result["status"] = "success"
    return status_result


def get_historical_data_by_country(country: str, last_days=30):
    last_days += 1 # Adding extra day slack for reducing daily data later
    country_data = {}
    req_url = serverURL + historicalRequestSuffix + country
    req_params = {'lastdays': last_days}
    response = requests.get(url=req_url, params=req_params)
    json_data = response.json()

    timeline = json_data.get("timeline")
    if timeline is not None:
        country_data = {"name": json_data.get("country"),
                        "cases": timeline.get("cases"),
                        "recovered": timeline.get("recovered"),
                        "deaths": timeline.get("deaths"),
                        "last_updated": datetime.utcnow()}

    return country_data


# class CountryData(object):
#     def __init__(self, json_data):
#         self.name = json_data.get("country")
#         timeline = json_data.get("timeline")
#         self.cases = timeline.get("cases")
#         self.recovered = timeline.get("recovered")
#         self.deaths = timeline.get("deaths")
