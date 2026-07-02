import argparse
import os

from dotenv import load_dotenv

# from google import genai
# from google.genai import types
from openai import OpenAI

# parser = argparse.ArgumentParser(description="Chatbot")
# parser.add_argument("user_prompt", type=str, help="User prompt")
# parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
# args = parser.parse_args()
# contents = args.user_prompt

# messages: list[types.Content] = [
#    types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
# ]

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY not set")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
# client = genai.Client(api_key=api_key)
response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
        },
    ],
)

# response = client.models.generate_content(
#    model="gemini-2.5-flash",
#    contents=messages,
# )

# if response.usage_metadata is None:
#    raise RuntimeError("no usage metadata returned")
#
# if args.verbose:
#    print(f"User prompt: {args.user_prompt}")
#    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
#    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

print(response.choices[0].message.content)
