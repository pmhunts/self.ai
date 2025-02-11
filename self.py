import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os
from datetime import datetime

def create_spreadsheet():
    """Create a sample DSA spreadsheet"""
    data = {
        'Month': ['January', 'February', 'March'],
        'Question ': [600, 650, 0],
        'Topics': [8, 6, 0],
        'Topics done': [3000, 600, 0],
        'total topics': [14, 6, 0],
        'Total Question': [0, 0, 0]
    }
    df = pd.DataFrame(data)
    return df

def send_spreadsheet(sender_email, sender_password, recipient_email):
    """Send spreadsheet via email"""
    try:
        # Create the spreadsheet
        df = create_spreadsheet()
        
        # Save to CSV
        filename = f"DSA_Report_{datetime.now().strftime('%Y%m%d')}.csv"
        df.to_csv(filename, index=False)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = "DSA Spreadsheet Report"
        
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

if __name__ == "__main__":
    # Replace these with your actual email credentials
    SENDER_EMAIL = "2k22.csai.2213601@gmail.com" # add your own Gmail
    SENDER_PASSWORD = "essf hfqm khco sfep"  # Use App Password for Gmail
    RECIPIENT_EMAIL = "2k22.csai.2213601@gmail.com" # add recipient Gmail
    
    result = send_spreadsheet(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)
    print(result)