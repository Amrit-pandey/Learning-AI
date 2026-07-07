from services.github import get_latest_repo

TOOLS_MAP = {
    "get_latest_repo": get_latest_repo
}

def execute_tools(name, arguments):
   tool = TOOLS_MAP.get(name)

   if tool is None:
    raise ValueError(f"Tool '{name}' not found")

   return tool(**arguments)