import requests

url = "https://golf-leaderboard-data.p.rapidapi.com/world-rankings"

headers = {
    'x-rapidapi-host': "golf-leaderboard-data.p.rapidapi.com",
    'x-rapidapi-key': "2f3de43532mshfdabba757fe2b87p106ddajsna8d5fd3d5639"
    }

response = requests.request("GET", url, headers=headers)

print(response.json())