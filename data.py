import requests
import datetime

def getYear(year):
    curve = requests.get("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/%s/all?type=daily_treasury_yield_curve&field_tdr_date_value=%s&page&_format=csv" % (str(year), str(year)))
    return parseData(curve.text)

def getCurrent():
    dt = datetime.datetime.today()
    year, month = dt.year, dt.month
    curr = str(year) + str("%02d" % month)
    curve = requests.get("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/%s?type=daily_treasury_yield_curve&field_tdr_date_value_month=%s&page&_format=csv" % (curr, curr))
    return parseDat(curve.text)

def getMonth(year, month):
    curr = str(year) + str("%02d" % month)
    curve = requests.get("https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/all/%s?type=daily_treasury_yield_curve&field_tdr_date_value_month=%s&page&_format=csv" % (curr, curr))
    return parseData(curve.text)

def parseData(raw):
    output = {}
    lines = raw.split("\n")
    categories = list(map(lambda x: x.replace('"', ''), lines[0][1:].split(",")))
    for i in range(1, len(lines)):
        items = lines[i].split(",")
        day = items[0].split("/")[1]
        row = {}
        for _ in range(1, len(items)):
            row[categories[_]] = float(items[_]) if items[_] != '' else None
        output[str(day)] = row
    return output
