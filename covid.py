import requests

url = "https://covid-19-data.p.rapidapi.com/report/totals"

querystring = {"date":"2020-08-08"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "2f3de43532mshfdabba757fe2b87p106ddajsna8d5fd3d5639"
    }

response = requests.request("GET", url, headers=headers)

print(response.json())