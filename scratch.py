import requests

url = "https://golf-leaderboard-data.p.rapidapi.com/world-rankings"

headers = {
    'x-rapidapi-host': "golf-leaderboard-data.p.rapidapi.com",
    'x-rapidapi-key': "API_KEY"
    }

response = requests.request("GET", url, headers=headers)

print(response.json())