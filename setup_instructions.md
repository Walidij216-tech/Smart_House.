# Setup Instructions

## Prerequisites

- Raspberry Pi 3 Model B+
- Raspberry Pi Camera
- BME280 I2C sensor
- Python 3
- Node.js

## Facial Recognition Setup

1. Install Python dependencies:
    ```sh
    pip install -r FacialRecognition/requirements.txt
    ```
2. Place training images in the `images/` directory.
3. Run the facial recognition script:
    ```sh
    python FacialRecognition/facial_recognition.py
    ```

## Temperature and Humidity Monitoring Setup

1. Install Node.js dependencies:
    ```sh
    cd TemperatureHumidityMonitoring
    npm install
    ```
2. Run the sensor script:
    ```sh
    node sensor.js
    ```

## Running the Project

Follow the individual component instructions to set up and run each part of the project. Ensure all hardware components are properly connected.
