import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
import requests
from datetime import datetime

def create_spreadsheet(leetcode_data):
 def create_spreadsheet():
    """Create a sample DSA spreadsheet 1"""
    data1 = {
        'Month': ['January', 'February', 'March'],
        'Question ': [600, 650, 500],
        'Topics': [8, 6, 4],
        'Topics done': [3000, 600, 400],
        'total topics': [14, 6, 8],
        'Total Question': [0, 0, 0]
    }
    df1 = pd.DataFrame(data1)
    # Include LeetCode data in the spreadsheet
    leetcode_df = pd.DataFrame(leetcode_data['stat_status_pairs'])
    df1 = pd.concat([df1, leetcode_df], axis=1)
    return df1

    return df1

 def create_spreadsheet1():
    """Create a sample DSA spreadsheet 2"""
    data2 = {
        'Month': ['April', 'May', 'June'],
        'Question ': [0, 0, 0],
        'Topics': [0, 0, 0],
        'Topics done': [0, 0, 0],
        'total topics': [0, 0, 0],
        'Total Question': [0, 0, 0]
    }
    df2 = pd.DataFrame(data2)
    return df2

 def create_spreadsheet2():
    """Create a sample DSA spreadsheet 3"""
    data3 = {
        'Month': ['July', 'August', 'September'],
        'Question ': [0, 0, 0],
        'Topics': [0, 0, 0],
        'Topics done': [0, 0, 0],
        'total topics': [0, 0, 0],
        'Total Question': [0, 0, 0]
    }
    df3 = pd.DataFrame(data3)
    return df3

def fetch_leetcode_data():
    """Fetch data from LeetCode API with error handling"""
    url = "https://leetcode.com/api/problems/all/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def send_spreadsheet(sender_email, sender_password, recipient_email, leetcode_data):
    """Send spreadsheet via email with error handling"""
    try:
        # Create the spreadsheet

        df1 = create_spreadsheet(leetcode_data)
        df2 = create_spreadsheet1()
        df3 = create_spreadsheet2()

        df1 = create_spreadsheet()
        df2 = create_spreadsheet1()
        
        # Save to CSV
        filename = f"DSA_Report_{datetime.now().strftime('%Y%m%d')}.csv"
        df1.to_csv(filename, index=False)
        df2.to_csv(filename, mode='a', header=False, index=False)
        df3.to_csv(filename, mode='a', header=False, index=False)
        
        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "DSA Spreadsheet Report"
        
        # Email body
        body = """
        Hello,

        Please find attached the DSA spreadsheet report.
        "Happy coding"

        Best regards,
        Your Automated System
        """
        msg.attach(MIMEText(body, 'plain'))
        
        # Attach spreadsheet
        with open(filename, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='csv')
            attachment.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(attachment)
        
        # Setup SMTP server (using Gmail as example)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        
        # Login and send email
        server.login(sender_email, sender_password)
        server.send_message(msg)
        
        # Clean up temporary file
        os.remove(filename)
        
        return "Email sent successfully!"  # Success message
    except Exception as e:
        return f"Error: {str(e)}"  # Error message
    finally:
        server.quit()  # Ensure server is closed

# Example usage
if __name__ == "__main__":
    SENDER_EMAIL = "2k22.csai.2213601@gmail.com"
    SENDER_PASSWORD = "hfwk yehy tofn xkzx"  # Use App Password for Gmail
    RECIPIENT_EMAIL = "2k22.csai.2213601@gmail.com"
    
    result = send_spreadsheet(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL, fetch_leetcode_data())
    SENDER_EMAIL = "2k22.csai.2213601@gmail.com" # Write a Sender Gmail
    SENDER_PASSWORD = "taem fumr twcm wbvi"  # Use App Password for Gmail
    RECIPIENT_EMAIL = "2k22.csai.2213601@gmail.com" # Write a Recipient Gmail
    
    result = send_spreadsheet(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)
    print(result)
