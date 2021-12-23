import requests

url = "https://covid-19-data.p.rapidapi.com/report/totals"

querystring = {"date":"2020-08-08"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "API_KEY"
    }

response = requests.request("GET", url, headers=headers)

print(response.json())