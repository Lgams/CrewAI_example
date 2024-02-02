from crewai import Agent, Task, Crew, Process
import os


os.environ["OPENAI_API_KEY"] = "INSERT-YOUR-API-KEY-HERE"  # Replace with your actual OpenAI API key

# Defining an agent for researching football news and trends
researcher = Agent(
    role='Researcher',
    goal='Football stories',
    backstory='You are a football professional.',
    verbose=True,
    allow_delegation=False
)

# Defining an agent for writing engaging articles about football
writer = Agent(
    role='Writer',
    goal='Write compelling and engaging articles about football.',
    backstory='You are a football post publisher who specializes in football.',
    verbose=True,
    allow_delegation=False
)

# Task for the researcher to investigate the latest developments in football
task1 = Task(
    description='Investigate the latest developments, news, and predictions in the football scene for 2024 and beyond, focusing on technological, player, and strategic advancements.',
    agent=researcher
)

# Task for the writer to create an article based on the researcher's findings
task2 = Task(
    description='Using the researched information, write an insightful article about news and advancements in football for 2024 and offer predictions on the direction of the sport in the coming years.',
    agent=writer
)

# Creating a crew to manage the agents and tasks in a sequential process
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential
)

# Executing the tasks using the crew and print the results
result = crew.kickoff()

print("######################")
print(result)
