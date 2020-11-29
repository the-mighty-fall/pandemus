
import json
import requests

#site: https://covidtracking.com/data/api
#urls:
# us daily https://api.covidtracking.com/v1/us/daily.json
# 
#
#

sample_data = [{
    "date": 20201125,
    "states": 56,
    "positive": 12580021,
    "negative": 148116434,
    "pending": 14060,
    "hospitalizedCurrently": 89954,
    "hospitalizedCumulative": 555727,
    "inIcuCurrently": 17526,
    "inIcuCumulative": 29540,
    "onVentilatorCurrently": 5989,
    "onVentilatorCumulative": 3147,
    "recovered": 4835545,
    "dateChecked": "2020-11-25T24:00:00Z",
    "death": 253210,
    "hospitalized": 555727,
    "totalTestResults": 184633681,
    "lastModified": "2020-11-25T24:00:00Z",
    "total": 0,
    "posNeg": 0,
    "deathIncrease": 2284,
    "hospitalizedIncrease": 4615,
    "negativeIncrease": 1147028,
    "positiveIncrease": 182537,
    "totalTestResultsIncrease": 1700638,
    "hash": "444fa3e2dfea0ba8c812ff6c524f58cf8e09e9a7"
}]

def request_data_as_json(url):
    resp = requests.request("GET", url)
    data_as_json = resp.text.encode('utf8')
    return data_as_json
