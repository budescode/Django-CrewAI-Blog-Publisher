from crewai import Agent, Process, Task, Crew, LLM
from blog_ai.agents.tools import BlogUploadTool
from agents.agent import llm, researcher, writer, research, write,  publisher, publish

# Assemble a crew with planning enabled
crew = Crew(
    agents=[researcher, writer,publisher],
    tasks=[research, write, publish],
    process=Process.sequential,
    verbose=True,
    planning=True,  # Enable planning feature
)
