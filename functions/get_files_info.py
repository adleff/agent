import os


def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        if not os.path.commonpath([target_dir, working_dir_abs]) == working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(f"{target_dir}"):
            return f'Error: "{directory}" is not a directory'

        files = os.listdir(target_dir)
        file_contents = []
        for file in files:
            full_path = os.path.join(target_dir, file)
            file_contents.append(
                f"- {file}: "
                f"file_size={os.path.getsize(full_path)} bytes, "
                f"is_dir={os.path.isdir(full_path)}"
            )
        return "\n".join(file_contents)

    except Exception as e:
        return f"Error: {str(e)}"
