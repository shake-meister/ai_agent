import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):

    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    # check file isnt outside of working directory.
    if not abs_file_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # check file is a file.
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    
    # check it has a python extension
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(timeout=30,
                                capture_output=True,
                                text=True,
                                cwd=os.path.abspath(working_directory),
                                args=["python", abs_file_path, *args] )
        
        msg = []
        if result.stdout:
            msg.append(f"STDOUT: {result.stdout}")
        
        if result.stderr:
            msg.append(f"STDERR: {result.stderr}")

        if result.returncode != 0:
            msg.append(f"Process exited with code {result.returncode}")
        
        return  "No output produced." if msg == [] else "/n".join(msg)

    except Exception as e:
        return f"Error: executing Python file: {e}"
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
    