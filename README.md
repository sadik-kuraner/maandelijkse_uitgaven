# Monthly Expenses

A simple Python application for tracking and managing monthly expenses, organized by categories.

## Features

- **Expenses by Category**: Manage expenses in three categories: personal, business, and misc
- **Add and Remove**: Easily add or remove expenses
- **Persistent Storage**: Data is saved in JSON format
- **Auto Load**: Previous data is automatically loaded on startup

## Installation

### Requirements
- Python 3.13 or higher

### Steps

1. Clone or download this project
2. Open a terminal and navigate to the project directory
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate the virtual environment:
   ```bash
   # macOS/Linux
   source venv/bin/activate
   
   # Windows
   venv\Scripts\activate
   ```

## Usage

Start the application with:
```bash
python main.py
```

The app will guide you step by step through the process:
1. Select a category (personal, business, or misc)
2. Choose whether you want to add or remove an expense
3. Enter the details
4. Your data is automatically saved

## Project Structure

```
maandelijkse_uitgaven/
├── main.py                              # Application entry point
├── functions.py                         # Core functionality
├── maandelijkse_uitgaven_overzicht.json # Saved data
├── README.md                            # This file
├── pyproject.toml                       # Project configuration
└── notities.txt                         # Notes
```

## Author

Sadik Kuraner
