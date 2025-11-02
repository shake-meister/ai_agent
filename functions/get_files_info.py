import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    

    dir_path = os.path.abspath(os.path.join(working_directory, directory))

    # check "directory" not outside of root folder
    if not dir_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    # check "directory" is a directory
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        # list everything in the folder and print each item in the form "- <item name>: file_size<size> bytes, is_dir=<True/False>"
        list_info = []#[f"Result for '{directory}' directory:"]
        for file_or_dir in os.listdir(dir_path):
            abs_file_or_folder = os.path.abspath(os.path.join(dir_path, file_or_dir))
            list_info.append(f" - {file_or_dir}: file_size={os.path.getsize(abs_file_or_folder)} bytes, is_dir={os.path.isdir(abs_file_or_folder)}")

        return "\n".join(list_info)
    except Exception as e:
        return f"Error listing files: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)