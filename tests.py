from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def get_files_tst():

    print(f"{get_files_info("calculator", ".")}\n")
    # Result for current directory:
    #  - main.py: file_size=719 bytes, is_dir=False
    #  - tests.py: file_size=1331 bytes, is_dir=False
    #  - pkg: file_size=44 bytes, is_dir=True

    print(f"{get_files_info("calculator", "pkg")}\n")
    # Result for 'pkg' directory:
    #  - calculator.py: file_size=1721 bytes, is_dir=False
    #  - render.py: file_size=376 bytes, is_dir=False

    print(f"{get_files_info("calculator", "/bin")}\n")
    # Result for '/bin' directory:
    #     Error: Cannot list "/bin" as it is outside the permitted working directory

    print(f"{get_files_info("calculator", "../")}\n")
    # Result for '/bin' directory:
    #     Error: Cannot list "/bin" as it is outside the permitted working directory

    return

def loram_ipsum_tst():
    result = get_file_content("calculator", "lorem.txt")
    print(result)
    print(f"words in the file: {len(result.split())}" )        
    return

def get_contents_tst():

    print(get_file_content("calculator", "main.py"))
    print(get_file_content("calculator", "pkg/calculator.py"))
    print(get_file_content("calculator", "/bin/cat"))  # (this should return an error string)
    print(get_file_content("calculator", "pkg/does_not_exist.py"))  # (this should return an error string)
    return

def write_tst():
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))

def basilisk():
    #print("           Running Tests               ")
    #print("")
    #print("--------------------------------------\n")
    #print('TESTING ("calculator", "main.py")')
    print(run_python_file("calculator", "main.py") )  # (should print the calculator's usage instructions)
    #print("")
    #print('TESTING ("calculator", "main.py" , ["3 + 5"])')
    print(run_python_file("calculator", "main.py", ["3 + 5"]))  # (should run the calculator... which gives a kinda nasty rendered result)
    #print("")
    #print('TESTING ("calculator", "tests.py")')
    print(run_python_file("calculator", "tests.py"))
    #print("")
    print(run_python_file("calculator", "../main.py"))  # (this should return an error)
    #print("")
    print(run_python_file("calculator", "nonexistent.py"))  # (this should return an error)
    #print("")
    print(run_python_file("calculator", "lorem.txt"))  # (this should return an error)

if __name__ == "__main__":

   # get_files_tst()
   # loram_ipsum_tst()
   # get_contents_tst()
   # write_tst()
   basilisk()
