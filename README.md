# Password Strength Checker with Suggestions

## Introduction

This project is a Python-based application that assesses the strength of passwords and provides suggestions for stronger alternatives. Built using PySide6 for the graphical user interface (GUI), this tool enables users to check their password strength, view password suggestions based on the input, and copy suggested passwords to the clipboard.

## Features

- **Password Strength Checker**: Evaluates the strength of a password based on length, presence of uppercase and lowercase letters, numbers, and special characters.
- **Password Suggestions**: Generates and displays password suggestions that are similar to the user input.
- **Show/Hide Password**: Allows users to toggle the visibility of their password input.
- **Copy Password**: Provides a "Copy" button next to each suggested password that appears on hover, enabling easy copying to the clipboard.
- **User-Friendly Interface**: Designed with a clean layout and interactive elements for a better user experience.

## Usage

1. **Run the Application**: Execute the script using Python. Ensure that you have `PySide6` installed.
   ```bash
   python Password_Checker.py
   ```
2. **Check Password Strength**: Enter a password into the input field. The application will display feedback on the strength of the password.

3. **View Suggestions**: As you type, password suggestions will appear below the input field.

4. **Show/Hide Password**: Use the "Show" button to reveal the password or "Hide" to obscure it.

5. **Copy Password**: Hover over a suggested password to reveal the "Copy" button. Click the button to copy the password to the clipboard.

## Requirements

- Python: Ensure Python 3.x is installed.
- PySide6: Install the required library using pip.
    ```bash
    pip install PySide6
    ```
