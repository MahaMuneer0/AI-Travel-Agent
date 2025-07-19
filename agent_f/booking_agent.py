from agents import Agent
from tools import getflight, suggest_hotel

booking_agent = Agent(
    name="BookingAgent",
    instructions="Use tools to get flights and suggest hotels for the selected destination.",
    tools=[getflight, suggest_hotel],
)
