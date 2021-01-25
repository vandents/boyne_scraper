from selenium import webdriver
import time
from chromedriver_py import binary_path
import smtplib
from datetime import datetime


# Function to send an email about available tickets
def send_email():
  message = 'Subject: {}\n\n{}'.format("Boyne tickets are available", "Get while the gettin's good")
  fromaddr = '<SENDER EMAIL>'
  toaddrs  = ['<RECEIVER EMAIL>', '<RECEIVER EMAIL>']

  # Set up email server and send message
  server = smtplib.SMTP('smtp.gmail.com', 587)
  server.starttls()
  server.login("<SENDER EMAIL>", “<SENDER PASSWORD>”)
  server.sendmail(fromaddr, toaddrs, message)
  server.quit()
  print("Email sent.")


# URL to lift ticket calendar
url = 'https://shop.boynemountain.com/s/lift-tickets/c/open-to-close-lift-ticket-boyne-mountain'

# Launch Chrome
driver = webdriver.Chrome(executable_path=binary_path)


while True:
  # Refresh page
  driver.get(url)

  # Wait for page to load
  time.sleep(30)

  # Find disabled January 30 elements
  results = driver.execute_script("""
    return Array.prototype.slice.call(
      document.querySelectorAll('.-disabled-[data-date="30"][data-month="0"]')
    ).filter(function(x) { return true; });
  """)

  print("\n" + datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

  # This could be a bug and send an email if the page doesn't load correctly
  if not results:
    print("Tickets found, sending email...")
    send_email()
  else:
    print("No tickets found.")

  # 14.5 minutes
  time.sleep(870)

