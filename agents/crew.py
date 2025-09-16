from crewai import Process, Crew
from agents.agent import researcher, writer, research, write,  publisher, publish

# Assemble a crew with planning enabled
crew = Crew(
    agents=[researcher, writer,publisher],
    tasks=[research, write, publish],
    process=Process.sequential,
    verbose=True,
    planning=True,  
)
