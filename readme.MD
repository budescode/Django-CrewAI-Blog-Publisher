A simple Django blog application that uses an autonomous multi-agent system built with **CrewAI** to automate the content creation and publishing process. The AI crew researches a topic, writes a complete blog post, and publishes it directly to the Django database. It's designed to run on a scheduled basis, generating and publishing a new blog post periodically.

### Features

  * **Automated Content Generation:** An AI research analyst finds a trending topic and provides key points.
  * **AI-Powered Writing:** An AI content writer crafts a full-length, engaging blog post based on the researched topic.
  * **Automatic Publishing:** A dedicated AI publisher agent uses a custom tool to upload the final blog post to the Django database.
  * **Django Backend:** A robust and secure backend powered by the Django framework.

-----

### Technologies Used

  * **Django:** A high-level Python web framework that encourages rapid development and clean, pragmatic design.
  * **CrewAI:** An agentic framework for orchestrating role-playing, autonomous AI agents.
  * **OpenAI:** The language model provider used by the agents to perform tasks.
  * **Pydantic:** Used to create a structured argument schema for the custom tool, ensuring reliable data transfer between the agent and the Django app.

-----

### Getting Started

#### Prerequisites

  * Python 3.10 or later
  * `pip` (Python package installer)
  * A valid OpenAI API key
  * A valid Serper API key (for web search)

#### Installation

1.  **Clone the repository:**

    ```bash
    git clone git@github.com:budescode/Django-CrewAI-Blog-Publisher.git
    cd Django-CrewAI-Blog-Publisher
    ```

2.  **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a `.env` file in the root directory and add your API keys.

    ```env
    OPENAI_API_KEY="your_openai_api_key"
    SERPER_API_KEY="your_serper_api_key"
    DJANGO_SECRET_KEY="your django secret key"
    ```

5.  **Set up the Django application:**
    Apply the database migrations to create the necessary tables.

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

    ```

-----


The crew will then proceed with the tasks: researching, writing, and finally uploading the content to your Django database. You can monitor the progress through the verbose output in the terminal.

-----

### Project Structure

```
.
├── blog_ai/           # Django project root
├── blog/              # Django blog app
│   ├── models.py      # Contains the BlogPost model
│   ├── apps.py        # Contains scheduling code to run periodically
│   └── ...
├── agents/            # CrewAI agents and tasks
│   ├── agent.py       # Contains the agents
│   └── tools.py       # contains the tools used by the agents
│   └── crew.py        # contains the crew

├── manage.py          # The main script to run the server
├── requirements.txt   # Project dependencies
└── README.md
```


