import os
from dotenv import load_dotenv
from agents import AsyncOpenAI, Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, RunConfig,handoffs
from agent_f import booking_agent, destination_agent, explore_agent
import asyncio

# Load environment variables
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
url = os.getenv("BASE_URL")


# Initialize the OpenAI client
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url=url
)

# Initialize the model
Model = OpenAIChatCompletionsModel(
    model='gemini-2.0-flash',
    openai_client=external_client
)


config= RunConfig(
    model=Model,
      model_provider=external_client,
      tracing_disabled=True
)
# Define the travel agent
travel_agent = Agent(
    name="TravelDesignerAgent",
    instructions="""
    You are a smart travel planner. 
    Start by understanding the user's mood or interests, 
    then:
    1. Handoff to DestinationAgent to suggest a destination.
    2. Once destination is picked, handoff to BookingAgent to simulate bookings.
    3. Finally, handoff to ExploreAgent to recommend things to do there.
    """,
    handoffs=[destination_agent, booking_agent, explore_agent],
)

async def main():
    user_input=input("hey! Tell us about your Interest or mood to travel:")
    rezult=await Runner.run(travel_agent,user_input,run_config=config)
    # print("travel agent reponse :",rezult.final_output)
    user_input1=input((f"rezult:"))
    rezult1=await Runner.run(travel_agent,user_input1,run_config=config)
    print(rezult1.final_output)


asyncio.run(main())