github_tool = {
    "type": "function",
    "function": {
        "name": "get_latest_repo",
        "description": "Returns the user's latest GitHub repository.",
        "parameters": {
            "type": "object",
            "properties": {
                "username": {
                    "type": "string",
                    "description": "Github username"
                }
            },
            "required": ["username"]
        }
    }
}

weather_tool = {
    "type": "function",
    "function": {
        "name": "get_current_weather",
        "description": "Get the current weather of any city. Use this tool whenever the user asks about weather, temperature, humidity, rain or forecast.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city"
                }
            },
            "required": ["city"]
        }
    }
}