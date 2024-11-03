from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You're an experienced QA engineer. And You're providing a clear and structured answers."
            },
            {
                "role": "user",
                "content": "Please give me three most used test types in testing Web Apps. Please provide only manual testing types and not automated."
            }
        ]
    )

    print(response.choices[0].message.content)
    print(response.model)
    print(f"prompt-tokens: {response.usage.prompt_tokens}")
    print(f"completion-tokens: {response.usage.completion_tokens}")
    print(f"total-tokens: {response.usage.total_tokens}")

except Exception as e:
    print(f"Error: {e}")
