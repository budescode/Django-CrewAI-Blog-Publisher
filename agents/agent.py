from crewai import Agent, Task, LLM
# Importing crewAI tools
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
from agents.tools import BlogUploadTool



# Load environment variables from .env file
load_dotenv() # 

llm = LLM(
    model="openai/gpt-4o-mini", # call model by provider/model_name
    temperature=0.8,
    max_tokens=4000,
    top_p=0.9,
    frequency_penalty=0.1,
    presence_penalty=0.1,
    stop=["END"],
    seed=42
)

# Instantiate tools
search_tool = SerperDevTool()
blog_upload_tool = BlogUploadTool()


# Create agents
researcher = Agent(
    llm=llm,
    role='Senior AI Engineer and Research Analyst',
    goal='Provide a single topic for a blog post about the AI industry',
    backstory='An expert analyst with a keen eye for market trends.',
    tools=[search_tool],
    verbose=True
)

writer = Agent(
    llm=llm,
    role='Content Writer',
    goal='Craft engaging blog posts based on the topic provided by the research analyst',
    backstory='A skilled writer with a passion for technology.',
    tools=[search_tool],
    verbose=True
)

publisher = Agent(
    llm=llm,
    role='Blog Publisher',
    goal='Upload the blog post to the Django application using the tool provided for you. It includes title and content.',
    backstory='An organized and detail-oriented digital publishing assistant, responsible for ensuring that every blog post is uploaded correctly, formatted neatly, and published on time. With years of experience in content management systems.',
    tools=[blog_upload_tool],
    verbose=True
)



# Define tasks
research = Task(
    description='Research the latest trends in the AI industry and provide a single title.',
    expected_output='An intruiging topic for a blog post about the AI industry, along with key points and references.',
    agent=researcher

)

write = Task(
    description="Write an engaging blog post about the title provided by the research analyst.",
    expected_output='A 10-paragraph blog post formatted in markdown with engaging, informative, and accessible content, avoiding complex jargon.',
    agent=writer,
    context=[research] # Pass the output of the research task to the writer
    
)

publish = Task(
    description="Publish the blog post to the Django application using the custom BlogUploadTool.",
    expected_output='A confirmation message indicating the blog post was successfully uploaded.',
    agent=publisher,
    context=[write] # Pass the output of the write task to the publisher
    
)


