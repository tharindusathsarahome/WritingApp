# WritingApp

Welcome to WritingApp, a powerful Flask-based application that leverages the OpenAI API to assist you in generating various types of written content. Whether you need a professional email, a response for Fiverr, or any other text, WritingApp has you covered. The application provides a user-friendly interface and allows you to create and customize cards with specific input fields and desired output formats.

## Table of Contents
- [Setup](#setup)
  - [Unix and MacOS](#unix-and-macos)
  - [Windows](#windows)
  - [API Key Configuration](#api-key-configuration)
- [Usage](#usage)
  - [Starting the App](#starting-the-app)
  - [Creating Users](#creating-users)
- [Overview](#overview)

## Setup

### Unix and MacOS

1. Install modules via `VENV`:

    ```bash
    $ virtualenv env
    $ source env/bin/activate
    $ pip3 install -r requirements.txt
    ```

2. Set up Flask Environment:

    ```bash
    $ export FLASK_APP=run.py
    $ export FLASK_ENV=development
    ```

3. Start the app:

    ```bash
    $ flask run
    ```

### Windows

1. Install modules via `VENV`:

    ```bash
    $ virtualenv env
    $ .\env\Scripts\activate
    $ pip3 install -r requirements.txt
    ```

2. Set up Flask Environment:

    - CMD:
        ```bash
        $ set FLASK_APP=run.py
        $ set FLASK_ENV=development
        ```

    - Powershell:
        ```bash
        $ $env:FLASK_APP = ".\run.py"
        $ $env:FLASK_ENV = "development"
        ```

3. Start the app:

    ```bash
    $ flask run
    ```

### API Key Configuration

Before running the app, configure your API keys in the `apps/config.py` file:

```python
# OpenAI API key
OPENAI_API_KEY = '' 

# Email configuration
EMAIL_ID = " " 
EMAIL_APP_PASSWORD =" " 

# Google Login API key
GOOGLE_CLIENT_ID = " " 

# Stripe payment gateway API key
PAYMENT_API_KEY = ' ' 
```

## Usage

### Starting the App

Once the setup is complete, the app will run at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Creating Users

To access private pages, follow these steps:

1. Start the app via `flask run`.
2. Access the registration page to create a new user: [http://127.0.0.1:5000/register](http://127.0.0.1:5000/register).
3. Access the sign-in page to authenticate: [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login).

## Overview

WritingApp allows you to create and customize cards, each with unique functionality. Whether you need assistance in crafting professional emails or responses for platforms like Fiverr, WritingApp streamlines the process with an intuitive user interface. Explore the possibilities and make your written communication more efficient and effective.
