import os
import config
from google.genai import types
from config import CHAR_LIMIT

def get_file_content(working_directory, file_path):

    # check file isnt outside of working directory.
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # check file is a file.
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    # read the file and truncate at CHAR_LIMIT
    try:
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(config.CHAR_LIMIT + 1)

        if len(file_content_string) > config.CHAR_LIMIT:
            file_content_string = file_content_string[:config.CHAR_LIMIT] + f'[...File "{file_path}" truncated at 10000 characters]'
        
        return file_content_string
        
    except Exception as e:
        return f"Error: reading files: {e}"

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {CHAR_LIMIT} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
