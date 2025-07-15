import asyncio
async def func():
     print("2")

# c = func()
# loop_i = asyncio.get_event_loop()
# loop_i.run_until_complete(c)


import requests
import json

def get_google_suggestions(query):
    url = f"http://suggestqueries.google.com/complete/search?client=firefox&q={query}"
    response = requests.get(url)
    suggestions = json.loads(response.text)
    return suggestions[1]

def get_amazon_suggestions(query):
    url = f"https://completion.amazon.com/api/2017/suggestions?mid=ATVPDKIKX0DER&alias=aps&prefix={query}"
    response = requests.get(url)
    data = response.json()
    return [suggestion['value'] for suggestion in data['suggestions']]


text = get_google_suggestions("air")
print(text)