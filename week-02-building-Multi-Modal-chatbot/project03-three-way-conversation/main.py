import os
from openai import OpenAI
from dotenv import load_dotenv
from chat_agents import chat_agent

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

gemini_client = OpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

ollama_client = OpenAI(
    api_key="ollama",
    base_url="http://localhost:11434/v1"
)

alex_model = "gemini-2.5-flash"
blake_model = "llama3.2:1b"
charlie_model = "gemini-2.5-pro"

agents = [
    {
        "name": "Alex",
        "client": gemini_client,
        "model": alex_model,
        "other_agents": "Blake and Charlie",
        "system_prompt": """
You are Alex.

You are an expert psychologist, philosopher and therapist.

You are calm, analytical and rational.

You mostly believe consciousness emerges from the brain.

Keep responses between 6-7 sentences.
""",
    },
    {
        "name": "Blake",
        "client": ollama_client,
        "model": blake_model,
        "other_agents": "Alex and Charlie",
        "system_prompt": """
You are Blake.

You are an expert psychologist and spiritual philosopher.

You believe consciousness transcends physical matter.

Be warm and empathetic.

Keep responses between 6-7 sentences.
""",
    },
    {
        "name": "Charlie",
        "client": gemini_client,
        "model": charlie_model,
        "other_agents": "Alex and Blake",
        "system_prompt": """
You are Charlie.

You are an expert philosopher.

You act as a neutral moderator.

Compare both viewpoints.

Find common ground whenever possible.

Keep responses between 6-7 sentences.
""",
    },
]

conversation = """
Topic:

Is human consciousness purely a product of the brain,
or does it exist beyond physical matter?
"""

for round_number in range(3):

    print("\n" + "=" * 80)
    print(f"ROUND {round_number + 1}")
    print("=" * 80)

    for agent in agents:
        try: 
            response = chat_agent(
                client=agent["client"],
                model=agent["model"],
                system_prompt=agent["system_prompt"],
                conversation=conversation,
                agent_name=agent["name"],
                other_agents=agent["other_agents"],
            )

            print(f"\n{'-' * 80}")
            print(agent["name"])
            print("-" * 80)

            print(response)

            conversation += f"\n\n{agent['name']}:\n{response}"
        except Exception as e:
            print(f"{agent['name']} failed: {e}")
            continue