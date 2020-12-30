from datetime import datetime, timedelta


def process_country_daily_data(country_data : dict):
    country_data = convert_country_data_datestring_keys_to_datetime(country_data)
    max_date = max(country_data["cases"].keys())
    min_date = min(country_data["cases"].keys())
    country_data = process_deaths_and_recovered_daily_data(country_data, min_date, max_date)
    country_data = process_daily_new_cases_data(country_data, min_date, max_date)
    country_data = convert_country_data_datetime_keys_to_datestring(country_data)
    return country_data


def process_daily_new_cases_data(country_data, min_date : datetime, max_date : datetime):
    daily_new_cases_data = {}
    delta = timedelta(days=1)
    current_date = max_date
    yesterday_date = current_date - delta
    end_date = min_date
    while current_date > end_date:
        daily_new_cases_data[current_date] = \
            country_data["cases"][current_date] - country_data["cases"][yesterday_date]\
            + country_data["deaths"][current_date] + country_data["recovered"][current_date]
        current_date -= delta
        yesterday_date = current_date - delta
    country_data["cases"] = daily_new_cases_data
    return country_data


def process_deaths_and_recovered_daily_data(country_data: dict, min_date : datetime, max_date : datetime):
    country_data["deaths"] = process_accumulative_to_daily_data(country_data["deaths"], min_date, max_date)
    country_data["recovered"] = process_accumulative_to_daily_data(country_data["recovered"], min_date, max_date)
    return country_data


def process_accumulative_to_daily_data(accumulative_data : dict, min_date : datetime, max_date : datetime):
    return convert_accumulative_datetime_dict_to_daily(accumulative_data, min_date, max_date)


def convert_accumulative_datetime_dict_to_daily(accumulative_dict, min_date : datetime, max_date : datetime):
    daily_data = {}
    delta = timedelta(days=1)
    current_date = max_date
    yesterday_date = current_date - delta
    end_date = min_date
    while current_date > end_date:
        daily_data[current_date] = accumulative_dict[current_date] - accumulative_dict[yesterday_date]
        current_date -= delta
        yesterday_date = current_date - delta
    return daily_data


def convert_datestring_to_datetime(date_string):
    return datetime.strptime(date_string, '%m/%d/%y')


def convert_datetime_to_datestring(date):
    return date.strftime('%m/%d/%y')


def convert_dict_string_keys_to_datetime(dict_data : dict):
    converted_dict_data = {}
    for key, val in dict_data.items():
        date = convert_datestring_to_datetime(key)
        converted_dict_data[date] = val
    return converted_dict_data


def convert_dict_datetime_keys_to_string(dict_data : dict):
    converted_dict_data = {}
    for key, val in dict_data.items():
        date = convert_datetime_to_datestring(key)
        converted_dict_data[date] = val
    return converted_dict_data


def convert_country_data_datestring_keys_to_datetime(country_data: dict):
    country_data["cases"] = convert_dict_string_keys_to_datetime(country_data["cases"])
    country_data["recovered"] = convert_dict_string_keys_to_datetime(country_data["recovered"])
    country_data["deaths"] = convert_dict_string_keys_to_datetime(country_data["deaths"])
    return country_data


def convert_country_data_datetime_keys_to_datestring(country_data: dict):
    country_data["cases"] = convert_dict_datetime_keys_to_string(country_data["cases"])
    country_data["recovered"] = convert_dict_datetime_keys_to_string(country_data["recovered"])
    country_data["deaths"] = convert_dict_datetime_keys_to_string(country_data["deaths"])
    return country_data
