import os
from google.genai import types

def write_file(working_directory, file_path, content):
    
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # check file isnt outside of working directory.
    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    # check filepath exists.
    try:
        if not os.path.exists(os.path.dirname(abs_file_path)):
            os.mkdir(abs_file_path)
        
        # write the file
        with open(abs_file_path, "w") as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        return f"Error: writing file: {e}"
    


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
