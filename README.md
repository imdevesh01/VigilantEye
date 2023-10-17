# VigilantEye - Human Invasion Detection

## Project Overview
VigilantEye is a human invasion detection system that uses computer vision to monitor a specified area. This project utilizes OpenCV, cv2, IP Webcam, and Twilio to detect unauthorized human presence and send SMS alerts in real-time. The primary goal of this project is to enhance security and monitoring in various environments, including homes, offices, or any location where unauthorized access is a concern.

## Features
- Real-Time Human Detection: VigilantEye employs OpenCV for real-time human detection using the video feed from an IP Webcam.

- WhatsApp Alert: Whenever human intrusion is detected, the system sends WhatsApp alert using Twilio to the designated recipient along with the photo of intruder.

- SMS Alerts: Whenever human intrusion is detected, the system sends SMS alerts using Twilio to the designated recipient.

- Configurable Parameters: You can configure the sensitivity, detection area, and other parameters to adapt the system to different monitoring scenarios.

- Customizable Recipients: Specify the phone number(s) to receive SMS alerts.

- Logging: Log events and alerts for future reference.

## Prerequisites
Before using VigilantEye, make sure you have the following:

- Python (3.x recommended)
- OpenCV
- cv2
- IP Webcam App (for providing video feed)
- Twilio Account SID and Auth Token
- Twilio phone number

## Setup and Configuration
1. Clone the Repository:
   git clone https://github.com/imdevesh01/VigilantEye.git
   cd VigilantEye
   
2. Install Dependencies:
   pip install opencv-python
   pip install opencv-python-headless
   pip install twilio
   
4. Configuration:
   Open config.py and set your IP Webcam URL, Twilio credentials, phone numbers, and any other configuration options.

5. Run the Application:
   python vigilant_eye.py

## Usage
-- Start the IP Webcam app on your mobile device and note the URL it provides for the video feed.

-- Run the VigilantEye application.

-- The application will start monitoring the specified area using your webcam feed.

-- If a human is detected, the system will send an SMS alert to the designated recipient(s).

-- The event logs can be found in the event_logs.txt file for future reference.

## Contributing
  Contributions are welcome! If you'd like to contribute to VigilantEye, please follow the standard practices for forking the repository, creating a new branch for your work, and submitting pull requests.

## Contact
  For any questions or feedback, feel free to contact me at:
  Email: 12112033it@gmail.com
  We hope that VigilantEye enhances security and provides a valuable solution for human invasion detection. Thank you for using VigilantEye!


