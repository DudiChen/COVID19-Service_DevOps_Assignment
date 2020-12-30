import threading
from datetime import datetime, timedelta
from service.covid_api import coronaDataExtractor
from app.pattern.singleton import Singleton


class DataHandler(metaclass=Singleton):
    def __init__(self):
        self.country_data = None
        self.is_valid_country = False

    def fetch_country_data(self, country : str, last_days=30):
        is_valid_countryName = False
        if (not self.country_data) \
                or (self.country_data["name"] != country) \
                or (not self.has_updated_within_last_hour()):
            self.country_data = {}
            result = coronaDataExtractor.get_historical_data_by_country(country, last_days)
            if result is not None:
                self.country_data = result
                self.is_valid_country = True
            else:
                self.is_valid_country = False
        return self.country_data

    def get_new_cases_peak_data(self, country : str):
        self.fetch_country_data(country)
        maxCasesResult = {}
        if self.country_data and self.is_valid_country:
            maxCasesResult = self.get_date_of_max_value(self.country_data["cases"])
        return maxCasesResult

    def get_recovered_peak_data(self, country : str):
        self.fetch_country_data(country)
        maxRecoveredResult = {}
        if self.country_data and self.is_valid_country:
            maxRecoveredResult = self.get_date_of_max_value(self.country_data["recovered"])
        return maxRecoveredResult

    def get_deaths_peak_data(self, country : str):
        self.fetch_country_data(country)
        maxDeathsResult = {}
        if self.country_data and self.is_valid_country:
            maxDeathsResult = self.get_date_of_max_value(self.country_data["deaths"])
        return maxDeathsResult

    def has_updated_within_last_hour(self):
        return self.country_data and (datetime.utcnow() - self.country_data["last_updated"] <= timedelta(hours=1))

    def get_date_of_max_value(self, dataDict):
        maxCases = {"date": None, "amount": -1}
        for key, value in dataDict.items():
            if value > maxCases["amount"]:
                maxCases["date"] = key
                maxCases["amount"] = value
        return maxCases

    def check_api_service_status(self):
        return coronaDataExtractor.check_status()
