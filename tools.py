import json
from agents import function_tool
with open("Travel_data.json","r")as file:
    travel_data=json.load(file)

@function_tool
def getflight(destination:str):
    for dest in travel_data["destinations"]:
        if dest["name"].lower() == destination.lower()  :
            return ("your flight ", dest["flights"])
        return "no flights available for this destination"
@function_tool
def suggest_hotel(destination:str):
    for dest in travel_data["destinations"]:
        if dest["name"].lower() == destination.lower():
            return(f"your hotel is  {dest["hotels"] } ")
        return "no hotel located"
    

@function_tool
def suggest_destination_on_mood(mood:str):
    for dest in travel_data["destinations"]:
        if mood.lower() in dest["moods"]:
            return f"Based on your mood '{mood}', I suggest you visit {dest['name']}."
    return "Sorry, I couldn't find a destination that matches your mood."    