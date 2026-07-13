import os

from config import MAX_CHARS
from openai.types.chat import ChatCompletionToolParam


schema_get_file_content: ChatCompletionToolParam = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Returns file content at a specific file path relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path relative to the working directory",
                },
            },
        },
    },
}

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if not os.path.commonpath([file_abs, working_dir_abs]) == working_dir_abs:
            return (
                f'Error: Cannot list "{file_path}"'
                f" as it is outside the permitted working directory"
            )
        if not os.path.isfile(f"{file_abs}"):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(file_abs, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated'
                content += f" at {MAX_CHARS} characters]"
            return content

    except Exception as e:
        return f"Error: {str(e)}"
