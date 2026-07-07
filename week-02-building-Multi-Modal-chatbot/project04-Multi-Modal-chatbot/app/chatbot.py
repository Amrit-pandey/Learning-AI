from pprint import pprint
from config.clients import system_prompt, gemini_client, ollama_client
from tools.registry import TOOLS
from tools.executor import execute_tools
import json

def chat(message, history):
    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    for h in history:
        messages.append(
            {
                "role": h["role"],
                "content": h["content"][0]["text"]
            }
        )

    messages.append(
        {
            "role": "user",
            "content": message
        }
    )
    response = ollama_client.chat.completions.create(model="llama3.2:1b", messages=messages, tools=TOOLS)
    # response = ""
    # for chunk in response:
    #     if chunk.choices[0].delta.content:
    #         response +=chunk.choices[0].delta.content
    #     yield response
    print(type(response))
    print(response)
    print(response.model_dump())
    message = response.choices[0].message
    print(message)
    if message.tool_calls:
        messages.append(message)
        tool_call = message.tool_calls[0]
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        result = execute_tools(tool_name, arguments)
        print(result)
    
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
        })

        final = ollama_client.chat.completions.create(
        model="llama3.2:1b",
        messages=messages
        )
        return final.choices[0].message.content
    return message.content