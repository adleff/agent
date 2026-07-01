import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if not os.path.commonpath([file_abs, working_dir_abs]) == working_dir_abs:
            return (
                f'Error: Cannot write to "{file_path}"'
                f" as it is outside the permitted working directory"
            )
        if os.path.isdir(f"{file_abs}"):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(file_abs), exist_ok=True)
        with open(file_abs, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return str(e)
