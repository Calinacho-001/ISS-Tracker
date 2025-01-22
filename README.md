# ISS Tracker 🚀

## Description

The ISS Tracker🚀 is a Python application that tracks the location of the International Space Station (ISS) and notifies you via email when it is overhead and it's dark outside at your location. This project uses APIs to fetch ISS location and sunrise/sunset times, making it an exciting way to explore Python's integration with web APIs.

## Features

- Tracks the ISS location in real-time using the ISS API.
- Determines if the ISS is overhead based on your geographical location.
- Checks if it's dark outside using the Sunrise-Sunset API.
- Sends email notifications when the ISS is visible from your location.

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `smtplib`
  - `datetime`

## How to Run

1. **Clone or Download the Project**:

   Download the project files and ensure all files are in the same directory.

2. **Install Required Libraries**:

   Install the necessary libraries by running:
   ```
   pip install requests
   ```

3. **Set Up Your Configuration**:

   - Open the `config.py` file and update the following:
     - `MY_LAT`: Your latitude.
     - `MY_LONG`: Your longitude.
     - `MY_EMAIL`: Your email address.
     - `PASSWORD`: Your email app password (configured in your email settings).

4. **Run the Script**:

   Execute the main script by running:
   ```
   python main.py
   ```

5. **What Happens**:

   - The script checks the ISS location and determines if it is overhead.
   - It checks if it is dark at your location.
   - If both conditions are true, you will receive an email notification.

## How It Works

- The script fetches the ISS's current location using the ISS API (`http://api.open-notify.org/iss-now.json`).
- It checks your local sunrise and sunset times using the Sunrise-Sunset API (`https://api.sunrise-sunset.org/json`).
- If the ISS is within 5 degrees of your location and it's dark, an email notification is sent.

## Files in the Project

- **`main.py`**: Contains the main logic for tracking the ISS and sending email notifications.
- **`config.py`**: Stores configuration details like your latitude, longitude, email, and app password.

## Future Improvements

- Add a graphical user interface (GUI) for easier interaction.
- Expand functionality to include other celestial events or objects.
- Log notifications for historical tracking.

## Credits

This project was created as a personal endeavor to explore Python's capabilities with web APIs and automation. It serves as a learning tool and a way to experiment with real-time data.

## Change Log

### Version 1.0.0

- **Initial Release**:
  - Tracks ISS location and checks visibility.
  - Sends email notifications when conditions are met.

### Known Issues

- No known issues at this time.

