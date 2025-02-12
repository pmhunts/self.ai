import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from datetime import datetime

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

def send_spreadsheet(sender_email, sender_password, recipient_email):
    """Send spreadsheet via email"""
    try:
        # Create the spreadsheet
        df1 = create_spreadsheet()
        df2 = create_spreadsheet1()
        
        # Save to CSV
        filename = f"DSA_Report_{datetime.now().strftime('%Y%m%d')}.csv"
        df1.to_csv(filename, index=False)
        df2.to_csv(filename, mode='a', header=False, index=False)

        
        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "DSA Spreadsheet Report"
        
        # Email body
        body = """
        Hello,

        Please find attached the DSA spreadsheet report.

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
        server.quit()
        
        # Clean up temporary file
        os.remove(filename)
        
        return "Email sent successfully!"
    
    except Exception as e:
        return f"Error sending email: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Replace these with your actual email credentials
    SENDER_EMAIL = "2k22.csai.2213601@gmail.com"
    SENDER_PASSWORD = "taem fumr twcm wbvi"  # Use App Password for Gmail
    RECIPIENT_EMAIL = "2k22.csai.2213601@gmail.com"
    
    result = send_spreadsheet(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)
    print(result)
