DSA Report Email Automation:-

This Python script automates the creation and email distribution of DSA (Data Structures and Algorithms) progress reports using spreadsheets. The script generates two sample spreadsheets with progress data and combines them into a single CSV file that is then emailed to specified recipients.
Features

Creates two sample DSA progress spreadsheets
Combines spreadsheets into a single CSV report
Automatically emails the report using SMTP (Gmail)
Includes timestamp in report filename
Cleans up temporary files after sending

Prerequisites

Python 3.x
Required Python packages:

pandas
smtplib (built-in)
email (built-in)



Install required packages using:
 {bashCopypip install pandas}

Setup :-

Enable 2-Step Verification in your Google Account
Generate an App Password:

Go to Google Account Settings > Security
Select "App Passwords" under 2-Step Verification
Generate a new app password for "Mail"


Use this App Password in the script instead of your regular Gmail password

Usage

Update the email credentials in the script:

pythonCopySENDER_EMAIL = "your-email@gmail.com"
SENDER_PASSWORD = "your-app-password"
RECIPIENT_EMAIL = "recipient@example.com"

Run the script:

bashCopypython dsa_report.py
Functions
create_spreadsheet()
Creates the first sample DSA spreadsheet with data for January through March.
create_spreadsheet1()
Creates the second sample DSA spreadsheet with empty data for April through June.
send_spreadsheet(sender_email, sender_password, recipient_email)
Combines the spreadsheets and sends them via email. Returns a success message or error details.
Output Format
The generated CSV file includes the following columns:

Month
Question
Topics
Topics done
total topics
Total Question

Security Notes

Never commit your email credentials to version control
Use environment variables or a configuration file for sensitive data
Always use App Passwords instead of your main Google account password

Error Handling
The script includes basic error handling and will return error messages if:

Email credentials are incorrect
SMTP connection fails
File operations fail

Contributing
Feel free to fork this repository and submit pull requests for any improvements.
License
This project is open source and available under the MIT License.
