# Personal Book Manager

A simple book management program built with Python. It allows users to add books, display them, and save them for future use.

![Python](https://img.shields.io/badge/Python-3-blue?=white)

## Features

- Add multiple books
- Display the list of books
- Save books in a JSON file
- Load previously saved books
- Admin Mode with a password stored in an environment variable

## Requirements

- Python
- python-dotenv

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project directory.

Use `.env.example` as a template and add your own password:

```dotenv
BOOK_MANAGER_ADMIN_PASSWORD=your_password_here
```

Replace `your_password_here` with your own password.

Do not upload your `.env` file to GitHub because it contains private configuration.

## Run the Program

Run the following command from the project directory:

```bash
python main.py
```

## Screenshot

### welcome
![Program Screenshot](images/welcome.jpg)

### admin mode
![Program Screenshot](images/adminmode.jpg)

### getbook
![Program Screenshot](images/getbook.jpg)

## Demo
![Program Screenshot](images/demo.gif)