import os

from dotenv import load_dotenv
from openai import OpenAI, omit
from openai._types import Omit
from openai.types.chat import ChatCompletionMessage
from openai.types.chat import ChatCompletionToolUnionParam
from collections.abc import Iterable

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    raise RuntimeError("OPENROUTER_API_KEY not set")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

def generate(
    messages,
    tools: Iterable[ChatCompletionToolUnionParam] | Omit = omit,
    model="openrouter/free"
) -> ChatCompletionMessage:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
    )
    return response.choices[0].message
