# Learning-AIProject 01 - Hello Gemini

My first Generative AI project built using Python and Google's Gemini API.

Objective

The goal of this project is to:

Learn Python project setup using UV
Work with virtual environments
Store API keys securely using .env
Connect to Gemini API
Send prompts and receive AI-generated responses
Build a strong foundation for future GenAI projects
Project Structure

project01-hello-gemini/

├── main.py

├── .env

├── .gitignore

├── pyproject.toml

├── uv.lock

└── README.md

Installation

Create virtual environment and install dependencies:

uv sync

Run the project:

uv run python main.py
Dependencies
google-genai
python-dotenv
Environment Variables

Create a .env file:

GEMINI_API_KEY=YOUR_API_KEY

Load the key in Python:

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
Features
Loads API key from environment variables
Validates API key
Sends prompt to Gemini
Prints AI response in terminal
Lessons Learned
1. Gemini SDK is different from OpenAI SDK

Initially I tried to use OpenAI-style messages:

messages = [
    {
        "role": "user",
        "content": "Hello"
    }
]

This caused validation errors.

Correct Gemini usage:

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Hello"
)
2. Virtual Environment Python Was Hanging

Problem:

.venv/bin/python --version

The command was hanging and not returning output.

Root Cause:

The project was using a UV-managed Python 3.12 interpreter which became problematic on my machine.

Fix:

Updated .python-version

echo "3.14" > .python-version

Recreated virtual environment:

rm -rf .venv
uv sync

After recreating the environment, Python worked correctly.

3. VS Code Could Not Detect Packages

Problem:

VS Code showed:

Package 'google-genai' is not installed in the selected environment

Even though packages were installed.

Fix:

Opened the project folder directly in VS Code:

project01-hello-gemini

And check -> run command 
which python
it gives you to the exact path.
then copy the path and press cmd+space+p then select python interpreter then you can see the list of interpreters and select .venev/bin/python. if not then press enter interpreter path and then paste the path that you have copied earlier and then press enter, That's it! 

Selected the correct Python interpreter.

After reloading VS Code, IntelliSense and package detection started working.

4. Import Suggestions Were Missing

Problem:

No autocomplete
Imports not highlighted
Pylance not detecting packages

Fix:

Installed Python extension
Installed Pylance extension
Selected correct interpreter
Reloaded VS Code
Commands Used During Setup

Check Python version:

python3 --version

Check UV version:

uv --version

List installed packages:

uv pip list

Create environment:

uv sync

Run project:

uv run python main.py

Activate environment:

source .venv/bin/activate
Future Improvements
Chat history support
Streaming responses
Image understanding
Multi-turn conversations
RAG integration
AI agents
LangChain integration
Author

Amrit Pandey

Learning Generative AI from scratch by building real projects and pushing them to GitHub.