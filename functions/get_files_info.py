import os


def get_files_info(working_directory: str, directory: str = ".") -> str:

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        if not os.path.commonpath([target_dir, working_dir_abs]) == working_dir_abs:
            return (
                f'Error: Cannot list "{directory}"'
                f"as it is outside the permitted working directory"
            )

        if not os.path.isdir(f"{target_dir}"):
            return f'Error: "{directory}" is not a directory'

        files_info = []
        for file in os.listdir(target_dir):
            full_path = os.path.join(target_dir, file)
            files_info.append(
                f"- {file}: "
                f"file_size={os.path.getsize(full_path)} bytes, "
                f"is_dir={os.path.isdir(full_path)}"
            )
        return "\n".join(files_info)

    except Exception as e:
        return f"Error: {str(e)}"
