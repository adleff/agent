import argparse
import json
import os
from call_function import call_function


from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY not set")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
response = client.chat.completions.create(
    model="openrouter/free",
    messages=messages,
    tools=available_functions,
)

message = response.choices[0].message
if message.tool_calls:
    for tool_call in message.tool_calls:
        function_args = json.loads(tool_call.function.arguments or "{}")
        result_message = call_function(tool_call.function.name, function_args)
        if not result_message.content:
            raise Exception("tool call returned empty content")
        if args.verbose:
        #    print(f"Tool call: {tool_call.function.name}")
            print(f"-> {result_message['content']}")
        messages.append(result_message)
else:
    print(response.choices[0].message.content)

#if not response.usage:
#    raise RuntimeError("no usage metadata returned")

#if args.verbose:
#    print(f"User prompt: {args.user_prompt}")
#    print(f"Prompt tokens: {response.usage.prompt_tokens}")
#    print(f"Response tokens: {response.usage.completion_tokens}")
#    print(f"Response: {response.choices[0].message.content}")
#else:
#    print(response.choices[0].message.content)
