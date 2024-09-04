# auto_whatsapp
# WhatsApp Automation App

This is a simple web application built using Streamlit that allows users to automate sending WhatsApp messages at a specified time using the `pywhatkit` library.

## Features

- Input recipient phone number, message, and the time to send the message.
- Automatically schedules the WhatsApp message to be sent at the specified time.
- User-friendly interface for scheduling messages.

## Requirements

- Python 3.6 or higher
- Streamlit
- pywhatkit

## Installation

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/your-username/whatsapp-automation-app.git
2.  Navigate to the project directory.

    ```bash
    cd whatsapp-automation-app
3.  Create and activate a virtual environment
    ```bash

    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
4.  Install the required packages.
    ```bash
    pip install -r requirements.txt
5.  Alternatively, you can install the dependencies manually:

    ```bash
    pip install streamlit pywhatkit

6.   Run the Streamlit app.
     ```bash
     streamlit run app.py
7.  Open your web browser and go to the following URL:

arduino

http://localhost:8501
Use the web interface to enter the recipient's phone number (including the country code), the message you want to send, and the time (in 24-hour format) when you want to send the message.

Click the "Send Message" button to schedule the message.

Important Notes
The phone number must include the country code (e.g., +1 for USA, +91 for India).
The WhatsApp application must be installed and logged in on your computer, and your phone must have an active internet connection.
The pywhatkit.sendwhatmsg() function will open WhatsApp Web in your browser, so make sure you are logged in.
Troubleshooting
If you encounter any errors, ensure that all fields are correctly filled in and that your internet connection is stable.
The pywhatkit library depends on the time accuracy of your system, so ensure your system clock is accurate.
