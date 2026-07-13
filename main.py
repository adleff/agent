import argparse
import sys

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

for _ in range(20):

    message = generate(messages, available_functions)
    messages.append(message)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            if tool_call.type == "function":
                result_message = call_function(tool_call, verbose=args.verbose)
                if not result_message["content"]:
                    raise Exception("tool call returned empty content")
                messages.append(result_message)
    elif message.content:
        print("Final response:")
        print(message.content)
        break
    else:
        print("No content returned")
        sys.exit(1)
else:
    print("No final response")
    sys.exit(1)
