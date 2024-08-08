import subprocess
import sys
import venv
import os


# Function to create virtual environment
def create_virtual_environment(env_name):
    venv.create(env_name, with_pip=True)
    print(f"Virtual environment '{env_name}' created.")


# Function to upgrade pip
def upgrade_pip(env_name):
    # Path to the Python executable in the virtual environment
    python_executable = os.path.join(env_name, 'Scripts', 'python.exe' if os.name == 'nt' else 'bin/python')

    # Upgrade pip
    subprocess.check_call([python_executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    print("pip upgraded.")


# Function to install dependencies
def install_dependencies(env_name, requirements_file):
    # Path to the Python executable in the virtual environment
    python_executable = os.path.join(env_name, 'Scripts', 'python.exe' if os.name == 'nt' else 'bin/python')

    # Install pip packages from requirements file
    subprocess.check_call([python_executable, '-m', 'pip', 'install', '-r', requirements_file])
    print("Dependencies installed.")
# Function to run the main script
def run_main_script(env_name, script_name):
    # Path to the Python executable in the virtual environment
    python_executable = os.path.join(env_name, 'Scripts', 'python.exe' if os.name == 'nt' else 'bin/python')
    # Run the main script
    subprocess.check_call([python_executable, script_name])
    print(f"{script_name} executed.")

# Main function
def main():
    env_name = 'venv'  # Name of the virtual environment
    requirements_file = 'requirements.txt'  # Path to the requirements file
    main_script = 'FinalDRO.py'
    create_virtual_environment(env_name)
    upgrade_pip(env_name)
    install_dependencies(env_name, requirements_file)
    run_main_script(env_name, main_script)

if __name__ == '__main__':
    main()
