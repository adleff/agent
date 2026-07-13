import argparse

from call_function import call_function, available_functions
from llm import generate
from prompts import system_prompt

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

message = generate(messages, available_functions)
messages.append(message)

if message.tool_calls:
    for tool_call in message.tool_calls:
        if tool_call.type == "function":
            result_message = call_function(tool_call, verbose=args.verbose)
            print(f"-> {result_message['content']}")
            if not result_message["content"]:
                raise Exception("tool call returned empty content")
            messages.append(result_message)
else:
    print(message.content)
