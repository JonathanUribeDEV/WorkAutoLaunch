# Script Description

This Python script automates a series of tasks related to web development using tools like Visual Studio Code, PowerShell, and commands for PHP and NPM projects.

## Features

- Opens PowerShell with a specified folder path.
- Executes commands (e.g., `php artisan serve`, `npm run dev`) in the opened PowerShell window. For Laravel Purposes.
- Opens a new tab and splits it into multiple tabs to execute commands concurrently.
- Opens Visual Studio Code with the specified folder path.

## Requirements

- Python
- Visual Studio Code
- PowerShell
- `pyautogui`, `pygetwindow`, and `subprocess` Python modules

Make sure the necessary software is installed and accessible via the specified paths in the script.

## Usage

1. Ensure that the required modules are installed (`pyautogui`, `pygetwindow`, `subprocess`).
2. Update the script with your preferred folder paths for the project, Visual Studio Code, and PowerShell.
3. Run the script using Python: `python script.py`.
4. Optionally, you can pass arguments to the script to customize folder paths:

## Example

```python
python script.py --folder_path "your_folder_path" --vs_code_path "your_vs_code_path" --power_shell_title "your_power_shell_title"
```

Serching for help?

```python
python script.py --help
```

## **Creating a Desktop Shortcut for Launching the Script**

1. **Locate Your Python Script:**
    - Ensure you know the full path to your Python script (e.g., **`C:\path\to\your\script.py`**).
2. **Create a Shortcut:**
    - Right-click on your desktop.
    - Navigate to **`New`** > **`Shortcut`**.
3. **Specify the Script Path:**
    - In the "Type the location of the item" field, paste the full path to your Python executable (e.g., **`"C:\path\to\python.exe"`**) followed by the full path to your Python script (e.g., **`"C:\path\to\your\script.py"`**). and the args for the script
        
        
        To find where is located the python interpreter path:
        
        ```python
        import os
        import sys
        os.path.dirname(sys.executable)
        ```
        
        Example:
        
        ```powershell
        "C:\Users\Jonathan Pabon\AppData\Local\Programs\Python\Python311\pythonw.exe" "C:\Users\Jonathan Pabon\work" --folder_path "C:\Users\Jonathan Pabon\Documents\Dev\Tiendas\TVA"
        ```
        
        The args can be hardwritten in the script.
        
    - Click **`Next`**.
4. **Name Your Shortcut:**
    - Provide a name for your shortcut (e.g., "Work").
    - Click **`Finish`**.
5. **Optional: Customize Shortcut Icon:**
    - Right-click on the shortcut you created.
    - Select **`Properties`**.
    - In the **`Shortcut`** tab, click on **`Change Icon...`**.
    - Browse and select an icon for your shortcut (you can use the provided icon file or select from system icons).
    - Click **`OK`** to confirm.
6. **Run Your Script:**
    - Double-click on the desktop shortcut to execute your Python script with predefined configurations.

By following these steps, you can create a convenient desktop shortcut for launching your Python script with ease, improving your workflow efficiency in web development tasks.


