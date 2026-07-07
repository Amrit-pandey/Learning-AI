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