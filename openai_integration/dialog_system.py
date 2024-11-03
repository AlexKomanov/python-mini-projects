from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

try:
    client = OpenAI(api_key=os.getenv("OPEN_AI_KEY"))
    chat_log = []
    system_prompt = {
        "role": "system",
        "content": "You're an experienced QA engineer. And You're providing a clear and structured answers."
    }
    chat_log.append(system_prompt)
    while True:
        user_message = input("Enter your prompt here | or type 'quit' to finish: ")
        print(f"{chat_log = }")

        if user_message.lower() == "quit":
            break

        else:
            chat_log.append({"role": "user", "content": user_message})
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=chat_log
            )
            assistant_response = response.choices[0].message.content
            print(f"\nChatGPT: {assistant_response}\n")
            chat_log.append({"role": "assistant", "content": assistant_response})
            print("\n-------------- Tokens Usage --------------")
            print(f"prompt-tokens: {response.usage.prompt_tokens}")
            print(f"completion-tokens: {response.usage.completion_tokens}")
            print(f"total-tokens: {response.usage.total_tokens}")
            print("------------------------------------------\n")



except Exception as e:
    print(f"Error: {e}")
