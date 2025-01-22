import requests
from datetime import datetime
from config import *  # Import constants and configurations from the config file
import smtplib
import time

# ---------- Function to Check ISS Position ---------- #
def is_iss_overhead():
    """
    Check if the ISS is currently overhead based on the user's latitude and longitude.
    
    Returns:
        bool: True if the ISS is within ±5 degrees of the user's location, otherwise False.
    """
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raise an error for failed requests
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if ISS position is within 5 degrees of the user's location
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False

# ---------- Function to Check for Darkness ---------- #
def is_dark():
    """
    Check if it is currently dark at the user's location based on sunrise and sunset times.
    
    Returns:
        bool: True if it is dark (before sunrise or after sunset), otherwise False.
    """
    response = requests.get("https://api.sunrise-sunset.org/json", params=PARAMETERS)
    response.raise_for_status()  # Raise an error for failed requests
    data = response.json()

    # Extract sunrise and sunset times
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current hour
    time_now = datetime.now().hour

    # Check if the current time is before sunrise or after sunset
    if time_now >= sunset or time_now <= sunrise:
        return True
    return False

# ---------- Main Loop to Monitor ISS Location ---------- #
while True:
    print("Checking where ISS is...")
    time.sleep(60)  # Pause for 60 seconds before checking again

    # If the ISS is overhead and it is dark, send an email
    if is_iss_overhead() and is_dark():
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(user=MY_EMAIL, password=PASSWORD)  # Log in to the email server
                # Send the email
                server.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg="Subject: Look Up!\n\nThe ISS is overhead!"
                )
            print("ISS is overhead! Email sent.")
        except Exception as e:
            print(f"Failed to send email: {e}")
