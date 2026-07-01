import os


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
    if not os.path.commonpath([file_abs, working_dir_abs]) == working_dir_abs:
        return (
            f'Error: Cannot execute "{file_path}"'
            f" as it is outside the permitted working directory"
        )
    if not os.path.isfile(f"{file_abs}"):
        return f'Error: "{file_path}" does not exist or is not a regular file'
