import requests  # For making HTTP requests
import time  # For time operations

esp32_ip = "192.168.1.xxx"  # The IP address of the ESP32
url = f"http://{esp32_ip}/"  # URL for making HTTP requests to the ESP32

file_name = "gas_data.txt"  # Name of the file where the data will be written
threshold = 100  # Threshold value: Data above this value will be written to the file

def get_gas_level():
    """
    Gets the gas level from the ESP32 and converts it to an integer.
    """
    try:
        response = requests.get(url)  # Make a GET request to the ESP32
        if response.status_code == 200:
            gas_level = int(response.text.strip())  # Convert the response to an integer
            return gas_level
        else:
            print(f"Error: HTTP response error - {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def main():
    """
    Main program loop: Gets the gas level from the ESP32, checks the threshold, and writes to the file.
    """
    while True:
        gas_level = get_gas_level()  # Get the gas level from the ESP32
        if gas_level is not None:
            print(f"Gas Level: {gas_level}")
            if gas_level > threshold:
                with open(file_name, "a") as file:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    file.write(f"{timestamp} - Gas level: {gas_level}\n")  # Write the data to the file with timestamp
                print(f"Data written to {file_name}")  # Notify that the data has been written to the file
        time.sleep(10)  # Wait for 10 seconds

if __name__ == "__main__":
    main()
