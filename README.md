# Gas Level Monitoring System with ESP32 and Python

This project monitors gas levels using an ESP32 microcontroller and an MQ-2 gas sensor. Gas level data is transmitted over WiFi to a computer and logged if it exceeds a specified threshold.

## Overview

The system continuously monitors gas levels. When the gas level exceeds a threshold, the system logs the data with a timestamp to a file on the computer. This is useful for detecting hazardous gas leaks in various environments.

## Components

- **ESP32 Development Board**: Microcontroller with WiFi.
- **MQ-2 Gas Sensor**: Detects gases like LPG, methane, and smoke.
- **Breadboard and Jumper Wires**: For circuit connections.
- **Computer with Python**: To receive and log gas level data.

## How It Works

1. **ESP32 Setup**: 
   - Reads gas levels from the MQ-2 sensor.
   - Serves data via a web server on the ESP32.
   - Connects to a WiFi network and provides its IP address.

2. **Data Transmission**:
   - A Python script on a computer requests gas level data from the ESP32.
   - If the gas level exceeds the threshold, the data with a timestamp is logged.

3. **Data Logging**:
   - Gas level data is stored in a text file for monitoring and analysis.

## Requirements

- **ESP32 Development Environment**: Arduino IDE or PlatformIO.
- **Python 3**: With `requests` library installed.

## Setup

1. **Hardware**:
   - Connect the MQ-2 gas sensor to the ESP32.

2. **ESP32**:
   - Flash the ESP32 with the provided code to set up WiFi and the web server.

3. **Python Script**:
   - Run the script on your computer to start monitoring and logging gas levels.

## Usage

1. Power on the ESP32 and connect to WiFi.
2. Run the Python script on your computer.
3. Gas data is logged to `gas_data.txt` when levels exceed the threshold.

**Note**: Customize WiFi credentials and IP addresses in the code before deployment.
