import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        file_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        if not os.path.commonpath([file_abs, working_dir_abs]) == working_dir_abs:
            return (
                f'Error: Cannot execute "{file_path}"'
                f" as it is outside the permitted working directory"
            )
        if not os.path.isfile(f"{file_abs}"):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", file_abs]
        if args:
            command.extend(args)
        process = subprocess.run(
            command,
            cwd=working_dir_abs,
            text=True,
            capture_output=True,
            timeout=30,
        )
        output = []
        if process.returncode != 0:
            output.append(f"Process exited with code {process.returncode}")
        if not process.stdout and not process.stderr:
            output.append("No output produced")
        if process.stdout:
            output.append(f"STDOUT:\n{process.stdout}")
        if process.stderr:
            output.append(f"STDERR:\n{process.stderr}")
        return "\n".join(output)

    except Exception as e:
        return f"Error: {str(e)}"
