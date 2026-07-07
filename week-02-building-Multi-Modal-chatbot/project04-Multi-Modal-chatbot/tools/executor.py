from services.github import get_latest_repo
from services.weather import get_current_weather

TOOLS_MAP = {
    "get_latest_repo": get_latest_repo,
    "get_current_weather": get_current_weather
}

def execute_tools(name, arguments):
    tool = TOOLS_MAP.get(name)

    if tool is None:
        raise ValueError(f"Tool '{name}' not found")

    return tool(**arguments)
   