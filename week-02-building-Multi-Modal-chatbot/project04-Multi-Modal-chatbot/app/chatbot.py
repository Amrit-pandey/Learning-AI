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
    response = ollama_client.chat.completions.create(
        model="qwen2.5:7b", 
        messages=messages, 
        tools=TOOLS, 
        stream=False
    )
    message = response.choices[0].message
    # this is not the right approach to call tools and streaming together
    # Later i'll find the correct approach and implememt this
    if message.tool_calls:
        messages.append(message)
        print("Tool Calls:", message.tool_calls)
        print("Content:", message.content)
        tool_call = message.tool_calls[0]
        tool_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)
        result = execute_tools(tool_name, arguments)
    
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result)
        })

        final = ollama_client.chat.completions.create(
        model="qwen2.5:7b",
        messages=messages
        )
        yield final.choices[0].message.content
        return
    else:
        response = ollama_client.chat.completions.create(
            model="qwen2.5:7b", 
            messages=messages,
            stream=True
        )
        stream = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                stream +=chunk.choices[0].delta.content
            yield stream
    return message.content