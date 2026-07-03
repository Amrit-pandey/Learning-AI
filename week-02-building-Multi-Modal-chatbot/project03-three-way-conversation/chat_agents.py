from openai import OpenAI

def chat_agent(client: OpenAI, model: str, system_prompt: str, conversation: str, agent_name: str, other_agents: str):
    print(model, agent_name, other_agents)
    user_prompt = f"""
    you are {agent_name}, 
    You are currently in a discussion with {other_agents}.
    The conversations so far is:
    {conversation}
    Now continue the discussion.
    Respond ONLY as {agent_name}.
    Do not generate responses for anyone else.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    return response.choices[0].message.content
