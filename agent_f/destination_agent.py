from agents import Agent ,FunctionTool
import json
from tools import getflight, suggest_hotel , suggest_destination_on_mood

with open("Travel_data.json","r") as file:
    travel_data =json.load(file)

destination_agent=Agent(
    name="destination_agent",
    instructions="you are a travel agent greet user and suggest them best destinations based on their mood and interest",
    model="gemini-2.5-flash",
    tools=[suggest_destination_on_mood, suggest_hotel, getflight]
)    

