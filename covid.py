import requests

url = "https://covid-19-data.p.rapidapi.com/report/country/all"

querystring = {"date":"2020-04-01"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "2f3de43532mshfdabba757fe2b87p106ddajsna8d5fd3d5639"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)