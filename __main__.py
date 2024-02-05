import subprocess
import pyautogui
import pygetwindow as gw
import time
import argparse

def cd_to_folder_path(folder_path):
    """
    Function to change directory to the specified folder path in the active window.
    
    Args:
    - folder_path (str): The path of the folder to change to.
    """
    # Write the command to change directory
    pyautogui.write(f'cd \"{folder_path}\"')
    # Press enter to execute the command
    pyautogui.press('enter')
    # Wait for a short duration to ensure the command is executed
    time.sleep(1)

def new_tab():
    """
    Function to open a new tab in the active window.
    """
    # Press the keyboard shortcut to open a new tab (ctrl + shift + T)
    pyautogui.hotkey('ctrl', 'shift', 'T')
    # Wait for a short duration to ensure the new tab is opened
    time.sleep(2)

def execute_command(command):
    """
    Function to execute a specified command in the active window.
    
    Args:
    - command (str): The command to execute.
    """
    # Write the command
    pyautogui.write(command)
    # Press enter to execute the command
    pyautogui.press('enter')
    # Wait for a short duration to ensure the command is executed
    time.sleep(1)

def split_to_the_rigth_tab():
    """
    Function to split the active window into the right tab.
    """
    # Press the keyboard shortcut to split to the right tab (shift + alt + +)
    pyautogui.hotkey('shift', 'alt', '+')
    # Wait for a short duration to ensure the splitting action is completed
    time.sleep(1)

def main():

    """
    Main function to execute the script.

    Requirements:
    - python
    - vscode
    - pyautogui, pygetwindow, and subprocess modules are required.
    - Ensure that the necessary software (e.g., VS Code, powershell, python) is installed and accessible via the specified paths.   

    Feel free to customize this script according to your specific needs.
    """

    # List of commands to execute, add more here or create custom arrays commands for other functionalities
    commands = [
        'php artisan serve',
        'npm run dev'
    ]

    # Create argument parser
    parser = argparse.ArgumentParser(description='Process paths.')
    parser.add_argument('--folder_path', type=str, help='Path to the folder')
    parser.add_argument('--vs_code_path', type=str, help='Path to VS Code')
    parser.add_argument('--power_shell_title', type=str, help='Title of the PowerShell window')

    # Parse command-line arguments
    args = parser.parse_args()

    # Assign values to variables based on command-line arguments or defaults to local paths
    folder_path = args.folder_path if args.folder_path else r"C:\Users\Jonathan Pabon\Documents\Dev\laravel-hyper"
    vs_code_path = args.vs_code_path if args.vs_code_path else r"C:\Users\Jonathan Pabon\AppData\Local\Programs\Microsoft VS Code\code"
    power_shell_title = args.power_shell_title if args.power_shell_title else r'C:\windows\System32\WindowsPowerShell\v1.0\powershell.exe'
    
    # Open a PowerShell window and change directory to the specified folder path
    subprocess.Popen(f'start powershell -NoExit -Command "cd \\"{folder_path}\\""', shell=True)

    # Wait for a few seconds
    time.sleep(5)

    # Get the PowerShell windows with the specified title
    powershell_windows = gw.getWindowsWithTitle(power_shell_title)

    # Iterate over each PowerShell window
    for window in powershell_windows:
        
        window.activate()

        new_tab()

        for pos, command in enumerate(commands, 1):

            cd_to_folder_path(folder_path)
            execute_command(command)

            if pos != len(commands):
                split_to_the_rigth_tab()

        time.sleep(2)
    
    # Open Visual Studio Code with the specified folder path
    subprocess.Popen([vs_code_path, folder_path], shell=True)

    # Open folder with the specified folder path
    # subprocess.Popen(['explorer', folder_path], shell=True)

if __name__ == "__main__":
    main()